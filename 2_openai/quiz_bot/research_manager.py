import asyncio

from email_agent import email_agent
from planner_agent import SearchItem, WebSearchPlan, planner_agent
from quiz_agent import Quiz, quiz_agent
from quiz_writer import QuizDocumentData, quiz_writer_agent
from search_agent import search_agent
from writer_agent import FoundationalKnowledgeData, writer_agent

from agents import Runner, gen_trace_id, trace


class ResearchManager:
    async def run(self, query: str):
        """Run the deep research process, yielding the status updates and the final report"""
        trace_id = gen_trace_id()
        with trace("Quiz Trace", trace_id=trace_id):
            print(
                f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            )
            yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            print("Starting research...")
            search_plan = await self.plan_searches(query)
            print(search_plan)
            yield "Searches planned, starting to search..."  # Prints what is currently happening (better user experience)
            search_results = await self.perform_searches(search_plan)
            yield "Searches complete, writing report..."
            data = await self.create_foundational_knowledge(query, search_results)
            yield "Foundational data created, generating quiz..."
            qa_pairs = await self.create_qa_pairs(data)
            yield "Quiz generated, generating quiz document..."
            quiz_document = await self.generate_quiz_document(qa_pairs)
            yield "Quiz document generated, sending email..."
            await self.send_email(quiz_document)
            yield "Email sent, research complete"
            yield quiz_document.markdown_quiz_document

    async def plan_searches(self, query: str) -> WebSearchPlan:
        """Plan the searches to perform for the query"""
        print("Planning searches...")
        result = await Runner.run(
            planner_agent,
            f"Query: {query}",
        )
        print(f"Will perform {len(result.final_output.searches)} searches")
        return result.final_output_as(WebSearchPlan)

    async def perform_searches(self, search_plan: WebSearchPlan) -> list[str]:
        """Perform the searches to perform for the query"""
        print("Searching...")
        num_completed = 0
        tasks = [
            asyncio.create_task(self.search(item)) for item in search_plan.searches
        ]
        results = []
        for task in asyncio.as_completed(tasks):
            result = await task
            if result is not None:
                results.append(result)
            num_completed += 1
            print(f"Searching... {num_completed}/{len(tasks)} completed")
        print("Finished searching")
        return results

    async def search(self, item: SearchItem) -> str | None:
        """Perform a search for the query"""
        input = f"Search term: {item.query}\nReason for searching: {item.reason}"
        try:
            result = await Runner.run(
                search_agent,
                input,
            )
            return str(result.final_output)
        except Exception:
            return None

    async def create_foundational_knowledge(
        self, query: str, search_results: list[str]
    ) -> FoundationalKnowledgeData:
        """Write the report for the query"""
        print("Thinking about provided foundational knowledge...")
        input = f"Original query: {query}\nSummarized search results: {search_results}"
        result = await Runner.run(
            writer_agent,
            input,
        )

        print("Finished creating foundational knowledge")
        return result.final_output_as(FoundationalKnowledgeData)

    async def create_qa_pairs(
        self, foundational_knowledge: FoundationalKnowledgeData
    ) -> Quiz:
        """Write the quiz based on the foundational knowledge"""
        print("Thinking about quiz...")
        input = f"Foundational knowledge: {foundational_knowledge.markdown_foundational_knowledge}"
        result = await Runner.run(
            quiz_agent,
            input,
        )

        print("Finished writing quiz")
        return result.final_output_as(Quiz)

    async def generate_quiz_document(self, quiz: Quiz) -> QuizDocumentData:
        """Generate the quiz document in markdown format"""
        print("Generating quiz document...")
        input = f"Question, Answer, and Reasoning pairs: {quiz.questions}"
        result = await Runner.run(
            quiz_writer_agent,
            input,
        )
        print("Finished generating quiz document")
        return result.final_output_as(QuizDocumentData)

    async def send_email(self, report: QuizDocumentData) -> None:
        print("Writing email...")
        result = await Runner.run(
            email_agent,
            report.markdown_quiz_document,
        )
        print("Email sent")
