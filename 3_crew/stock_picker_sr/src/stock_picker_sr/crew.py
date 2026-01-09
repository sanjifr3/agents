from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.memory import EntityMemory, LongTermMemory, ShortTermMemory
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
from crewai.memory.storage.rag_storage import RAGStorage
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
            memory=True,
        )

    # No memory here so it goes out and does research
    @agent
    def financial_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["financial_researcher"], tools=[SerperDevTool()]
        )

    @agent
    def stock_picker(self) -> Agent:
        return Agent(
            config=self.agents_config["stock_picker"],
            tools=[PushNotificationTool()],
            memory=True,
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

        short_term_memory = ShortTermMemory(
            storage=RAGStorage(
                embedder_config={
                    "provider": "openai",
                    "config": {"model_name": "text-embedding-3-small"},
                },
                type="short_term",
                path="./memory/",
            )
        )

        long_term_memory = LongTermMemory(
            storage=LTMSQLiteStorage(db_path="./memory/long_term_memory_storage.db")
        )

        entity_memory = EntityMemory(
            storage=RAGStorage(
                embedder_config={
                    "provider": "openai",
                    "config": {"model_name": "text-embedding-3-small"},
                },
                type="entity",
                path="./memory/",
            )
        )

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            manager=manager,
            process=Process.hierarchical,
            verbose=True,
            manager_agent=manager,
            memory=True,
            short_term_memory=short_term_memory,
            long_term_memory=long_term_memory,
            entity_memory=entity_memory,
        )
