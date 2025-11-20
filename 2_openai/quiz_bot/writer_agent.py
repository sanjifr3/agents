from agents import Agent, Runner, trace
from models import gemini_model
from pydantic import BaseModel, Field

INSTRUCTIONS = """
You are a subject matter expert tasked with creating the foundational knowledge that a quiz questions will be based on.
You will be provided with the original query, and some initial research done by a research assistant.
You should first come up with topics for the quiz that describes the structure and flow of the quiz.
Then, generate a foundational knowledge document and return that as your final output.
The final output should be in markdown format, and it should be lengthy and detailed. Aim
for 5-10 pages of content, at least 1000 words.
"""


class FoundationalKnowledgeData(BaseModel):
    short_summary: str = Field(
        description="A short 2-3 sentence summary of the foundational knowledge."
    )

    markdown_foundational_knowledge: str = Field(
        description="The foundational knowledge document"
    )

    follow_up_questions: list[str] = Field(
        description="Suggested topics to expand the knowledge base further"
    )


writer_agent = Agent(
    name="Writer agent",
    instructions=INSTRUCTIONS,
    model=gemini_model,
    output_type=FoundationalKnowledgeData,
)
