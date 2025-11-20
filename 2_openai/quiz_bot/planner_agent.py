import asyncio

from agents import Agent, Runner, trace
from models import gemini_model
from pydantic import BaseModel, Field

N_SEARCHES = 5

INSTRUCTIONS = f"""
You are quiz planning assistant. Given a query, come up with a set of web searches 
to collect relevant information to create quiz questions. Output {N_SEARCHES} search terms 
to query for. Focus more on theory and concepts that would be tested on in a interview setting.
Focus more on basics and foundational knowledge.
"""


class SearchItem(BaseModel):
    reason: str = Field(
        description="Your reasoning for why this search is important to the query."
    )
    query: str = Field(description="The search term to use for the web search.")


class WebSearchPlan(BaseModel):
    searches: list[SearchItem] = Field(
        description="A list of web searches to perform to best answer the query."
    )


planner_agent = Agent(
    name="Planner agent",
    instructions=INSTRUCTIONS,
    model=gemini_model,
    output_type=WebSearchPlan,
)


async def main():
    with trace("Planner agent"):
        result = await Runner.run(planner_agent, "Machine Learning and AI")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
