from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class DebateSr:
    """DebateSr crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    ## Agents

    @agent
    def debater(self) -> Agent:
        return Agent(config=self.agents_config["debater"], verbose=True)

    @agent
    def judge(self) -> Agent:
        return Agent(config=self.agents_config["judge"], verbose=True)

    ## Tasks

    @task
    def propose(self) -> Task:
        return Task(
            config=self.tasks_config["propose"],  # type: ignore[index]
        )

    @task
    def oppose(self) -> Task:
        return Task(
            config=self.tasks_config["oppose"],  # type: ignore[index]
        )

    @task
    def decide(self) -> Task:
        return Task(
            config=self.tasks_config["decide"],  # type: ignore[index]
        )

    ## Crew

    @crew
    def crew(self) -> Crew:
        """Creates the DebateSr crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
