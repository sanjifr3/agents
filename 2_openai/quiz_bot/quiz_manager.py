import asyncio

from agents import Agent, Runner, gen_trace_id, trace
from email_agent import email_agent
from grader_agent import grader_agent
from models import gemini_model
from quiz_agent import quiz_agent

INSTRUCTIONS = """
You are a quiz manager agent that is responsible for orchestrating a quiz with a student.
You will be provided the foundational knowledge to base the quiz on,
and given access to a quiz agent to generate questions, answers with reasoning, and a grader agent to grade QA pairs.

You also have access to an email agent to send the foundational knowledge, and quiz to the student, should they request it.
If they request it, ensure to ask for their email address to send the email.
"""

quiz_manager_agent = Agent(
    name="Quiz manager agent",
    instructions=INSTRUCTIONS,
    tools=[quiz_agent, grader_agent, email_agent],
    model="gpt-4o-mini",
)


async def main():
    with trace("Quiz manager agent"):
        result = await Runner.run(
            quiz_manager_agent,
            "What is the role of governance in the use of generative AI?",
        )
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
