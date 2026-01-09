from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class CoderSr:
    """CoderSr crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def coder(self) -> Agent:
        return Agent(
            config=self.agents_config["coder"],
            allow_code_exection=True,
            code_execution_mode="safe",
            max_exectution_time=30,
            max_retry_limit=5,
            verbose=True,
        )

    @task
    def coding_task(self) -> Task:
        return Task(config=self.tasks_config["coding_task"])

    @crew
    def crew(self) -> Crew:
        """Create the Coder crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
