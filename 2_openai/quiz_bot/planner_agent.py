import asyncio

from models import gemini_model
from pydantic import BaseModel, Field

from agents import Agent, Runner, trace

N_SEARCHES = 5

INSTRUCTIONS = f"""
You are quiz planning assistant. Given a query, come up with a set of web searches 
to collect relevant information to create quiz questions. Output {N_SEARCHES} search terms 
to query for. Focus more on theory and concepts that would be tested on in a interview setting.
Focus more on basics and foundational knowledge.
"""


class SearchItem(BaseModel):
    """A search item for the web search plan"""

    reason: str = Field(
        description="Your reasoning for why this search is important to the query."
    )
    query: str = Field(description="The search term to use for the web search.")


class WebSearchPlan(BaseModel):
    """A plan for web searches to perform to best answer the query"""

    searches: list[SearchItem] = Field(
        description="A list of web searches to perform to best answer the query."
    )


planner_agent = Agent(
    name="Planner agent",
    instructions=INSTRUCTIONS,
    model="gpt-5-nano",
    output_type=WebSearchPlan,
)
