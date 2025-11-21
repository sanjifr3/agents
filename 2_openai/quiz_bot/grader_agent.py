import asyncio

from agents import Agent, Runner, trace
from models import gemini_model
from pydantic import BaseModel, Field

INSTRUCTIONS = """
You are a quiz grader agent that is given a question, groud truth answer and reasoning, and a student's answer.
Evaluate if the student's answer is correct and concise.
If the student's answer is correct, return the score and reasoning.
If the student's answer is incorrect, return the score and reasoning.
The reasoning should be concise and to the point.
"""


class Grade(BaseModel):
    """A list of questions and answers"""

    is_correct: bool = Field(description="Whether the student's answer is correct")
    reasoning: str = Field(description="The reasoning behind the grade")


grader_agent = Agent(
    name="Grader agent",
    instructions=INSTRUCTIONS,
    model=gemini_model,
    output_type=Grade,
)


async def main():
    with trace("Grader agent"):
        result = await Runner.run(
            grader_agent,
            """
            Question: What is the role of governance in the use of generative AI?
            Answer: To ensure responsible use through strong governance, transparency, and ethical guidelines.
            Reasoning: Governance is important for responsible use of generative AI.
            Student's Answer: Ensure the safe use of generative AI.
            """,
        )
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
