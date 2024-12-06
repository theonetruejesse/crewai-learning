from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ContentCrew():
	# crews folder pattern doesn't work well given config file bugs
	agents_config = '../config/agents.yaml'
	tasks_config = '../config/tasks.yaml'

	""" Agents """

	@agent
	def planner(self) -> Agent:
		return Agent(
			config=self.agents_config['planner'],
			verbose=True
		)

	@agent
	def writer(self) -> Agent:
		return Agent(
			config=self.agents_config['writer'],
			verbose=True
		)
	
	@agent
	def editor(self) -> Agent:
		return Agent(
			config=self.agents_config['editor'],
			verbose=True
		)
	
	""" Tasks """

	@task
	def plan_task(self) -> Task:
		return Task(
			config=self.tasks_config['plan_task'],
		)

	@task
	def write_task(self) -> Task:
		return Task(
			config=self.tasks_config['write_task'],
		)

	@task
	def edit_task(self) -> Task:
		return Task(
			config=self.tasks_config['edit_task'],
			output_file='content.md'
		)

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
