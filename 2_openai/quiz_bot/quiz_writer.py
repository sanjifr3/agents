from models import gemini_model
from pydantic import BaseModel, Field

from agents import Agent, Runner, trace

INSTRUCTIONS = """
You are given a set of question, answer, and reasoning pairs.
Given that information create a Markdown document that first contains the questions in a numbered list,
followed by the answers and reasoning in a separate section.
The final output should be in markdown format.
Aim for clarity and conciseness.
"""


class QuizDocumentData(BaseModel):
    markdown_quiz_document: str = Field(
        description="The final quiz document in markdown format."
    )


quiz_writer_agent = Agent(
    name="Quiz Writer agent",
    instructions=INSTRUCTIONS,
    model="gpt-5-nano",
    output_type=QuizDocumentData,
)
