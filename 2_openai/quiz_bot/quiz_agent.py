import asyncio

from models import gemini_model
from pydantic import BaseModel, Field

from agents import Agent, Runner, trace

INSTRUCTIONS = """
You are a quiz agent assigned to generate questions from a given foundational knowledge document.
You will be provided the foundational knowledge and from there you would generate questions and answers with reasoning
for each topic in the foundational knowledge document. 

For the reasoning field, explain WHY the answer is correct by providing the actual logic, explanation, or evidence that supports it. 
The reasoning should be educational and help someone understand the concept, not just cite that the document mentions it.
Do not use phrases like "the document says", "the foundational knowledge states", or "according to the document".
Instead, directly explain the concept, logic, or evidence that makes the answer correct.

Do not make up information that is not in the foundational knowledge.
Do not include any additional commentary other than the questions and answers with reasoning.
Do not mention that a document was provided.
The questions should be in the form of a quiz, including open ended questions, multiple choice, and true and false questions.
Generate a list of 20 questions and answers, across all topics in the foundational knowledge document.
"""


class QA(BaseModel):
    """A question and answer pair"""

    question: str = Field(description="The question to be asked from the student")
    answer: str = Field(description="The answer to the question")
    reasoning: str = Field(description="The reasoning behind the answer")


class Quiz(BaseModel):
    """A list of questions and answers"""

    questions: list[QA] = Field(description="The list of questions and answers")


quiz_agent = Agent(
    name="Quiz agent",
    instructions=INSTRUCTIONS,
    model="gpt-5-nano",
    output_type=Quiz,
)
