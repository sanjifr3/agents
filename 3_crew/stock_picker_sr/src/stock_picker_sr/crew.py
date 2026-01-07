from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field

from .tools.push_tool import PushNotificationTool


class TrendingCompany(BaseModel):
    """A company that is in the news and attracting attention."""

    name: str = Field(description="Company Name")
    ticker: str = Field(description="Stock Ticker Symbol")
    reason: str = Field(description="Reason this company is trending in the news")


class TrendingCompanyList(BaseModel):
    """List of trending companies."""

    companies: List[TrendingCompany] = Field(description="List of trending companies")


class TrendingCompanyResearch(BaseModel):
    """Research information about a trending company."""

    name: str = Field(description="Company Name")
    market_position: str = Field(
        description="Current market position and competitive analysis."
    )
    future_outlook: str = Field(description="Future outlook and growth prospects.")
    investment_potential: str = Field(
        description="Investment potential and suitability for investment."
    )


class TrendingCompanyResearchList(BaseModel):
    """List of research information about trending companies."""

    research: List[TrendingCompanyResearch] = Field(
        description="Comprehensive research on all trending companies"
    )


@CrewBase
class StockPickerSr:
    """StockPickerSr crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def trending_company_finder(self) -> Agent:
        return Agent(
            config=self.agents_config["trending_company_finder"],
            tools=[SerperDevTool()],
        )

    @agent
    def financial_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["financial_researcher"], tools=[SerperDevTool()]
        )

    @agent
    def stock_picker(self) -> Agent:
        return Agent(
            config=self.agents_config["stock_picker"], tools=[PushNotificationTool()]
        )

    @task
    def find_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config["find_trending_companies"],
            output_pydantic=TrendingCompanyList,
        )

    @task
    def research_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config["research_trending_companies"],
            output_pydantic=TrendingCompanyResearchList,
        )

    @task
    def pick_best_company(self) -> Task:
        return Task(
            config=self.tasks_config["pick_best_company"],
        )

    @crew
    def crew(self) -> Crew:
        manager = Agent(config=self.agents_config["manager"], allow_delegation=True)

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            manager=manager,
            process=Process.hierarchical,
            verbose=True,
            manager_agent=manager,
        )
