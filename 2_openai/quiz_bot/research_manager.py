import asyncio

from agents import Agent, Runner, gen_trace_id, trace
from email_agent import email_agent
from models import gemini_model
from planner_agent import SearchItem, WebSearchPlan, planner_agent
from quiz_manager import quiz_manager_agent
from search_agent import search_agent
from writer_agent import FoundationalKnowledgeData, writer_agent

INSTRUCTIONS = """
You are a research manager managing the generation of a foundational knowledge document based on the topic that
the student wants to be quizzed on.

You have access to a planner agent to plan the searches to perform, a search agent to conduct the search and return the results,
and a writer agent to write the foundational knowledge based on the search results.

You will then handoff the foundational knowledge to the quiz manager agent to be used to generate a quiz for the student.
Do not answer directly, only handoff the foundational knowledge to the quiz manager agent.
"""

research_manager_agent = Agent(
    name="Research manager agent",
    instructions=INSTRUCTIONS,
    tools=[planner_agent, search_agent, writer_agent],
    model="gpt-4o-mini",
    handoffs=[quiz_manager_agent],
)


# async def main():
#     with trace("Research manager agent"):
#         result = await Runner.run(
#             research_manager_agent,
#             "Generative AI",
#         )
#         print(result)


# if __name__ == "__main__":
#     asyncio.run(main())


# class ResearchManager:
#     async def run(self, query: str):
#         """Run the deep research process, yielding the tsatus updates and the final results"""

#         trace_id = gen_trace_id()
#         with trace("Research trace", trace_id=trace_id):
#             print(
#                 f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
#             )
#             yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
#             print("Starting quiz generation...")
#             search_plan = await self.plan_searches(query)
#             yield "Searches planned, starting to search..."  # Prints what is currently happening (better user experience)
#             search_results = await self.perform_searches(search_plan)
#             yield "Searches complete, writing foundational knowledge..."
#             foundational_knowledge = await self.create_foundational_knowledge(
#                 query, search_results
#             )
#             yield "Foundational knowledge generation completed. Beginning quiz generation..."
#             async for chunk in Runner.run_streamed(
#                 quiz_manager_agent,
#                 foundational_knowledge.markdown_foundational_knowledge,
#             ):
#                 yield chunk

#     async def plan_searches(self, query: str) -> WebSearchPlan:
#         """Plan the searches to perform for the query"""
#         print("Planning searches...")
#         result = await Runner.run(
#             planner_agent,
#             f"Query: {query}",
#         )
#         print(f"Will perform {len(result.final_output.searches)} searches")
#         return result.final_output_as(WebSearchPlan)

#     async def perform_searches(self, search_plan: WebSearchPlan) -> list[str]:
#         """Perform the searches to perform for the query"""
#         print("Searching...")
#         num_completed = 0
#         tasks = [
#             asyncio.create_task(self.search(item)) for item in search_plan.searches
#         ]
#         results = []
#         for task in asyncio.as_completed(tasks):
#             result = await task
#             if result is not None:
#                 results.append(result)
#             num_completed += 1
#             print(f"Searching... {num_completed}/{len(tasks)} completed")
#         print("Finished searching")
#         return results

#     async def search(self, item: SearchItem) -> str | None:
#         """Perform a search for the query"""
#         input = f"Search term: {item.query}\nReason for searching: {item.reason}"
#         try:
#             result = await Runner.run(
#                 search_agent,
#                 input,
#             )
#             return result.final_output
#         except Exception as e:
#             print(f"Error during search for {item.query}: {e}")
#             return None

#     async def create_foundational_knowledge(
#         self, query: str, search_results: list[str]
#     ) -> FoundationalKnowledgeData:
#         """Write the foundational knowledge for the quiz"""
#         print("Thinking about foundational knowledge...")
#         input = f"Original query: {query}\nSummarized search results: {search_results}"
#         result = await Runner.run(
#             writer_agent,
#             input,
#         )
#         return result.final_output_as(FoundationalKnowledgeData)

#     async def send_email(self, foundational_knowledge: FoundationalKnowledgeData):
#         """Send the foundational knowledge via email"""
#         print("Sending email...")
#         email_content = f"Subject: Foundational Knowledge Document\n\n{foundational_knowledge.markdown_foundational_knowledge}"
#         await Runner.run(
#             email_agent,
#             email_content,
#         )
#         print("Email sent.")
