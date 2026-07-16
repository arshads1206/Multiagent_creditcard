# graph.py

from app.agents.requirement_agent import requirement_agent
from app.agents.research_agent import research_agent
from app.agents.evaluation_agent import evaluation_agent
from app.agents.response_agent import response_agent

from app.models.schemas import Requirement


def run_workflow(query: str):

    print("\n========== Requirement Agent ==========\n")

    # Returns a dict
    requirement_dict = requirement_agent(query)
    print(requirement_dict)

    # Convert dict -> Requirement object
    requirement = Requirement(**requirement_dict)

    print("\n========== Research Agent ==========\n")

    research = research_agent(requirement)
    print(research)

    print("\n========== Evaluation Agent ==========\n")

    evaluation = evaluation_agent(
        requirement=requirement,
        research=research
    )
    print(evaluation)

    print("\n========== Response Agent ==========\n")

    response = response_agent(
        requirement=requirement,
        evaluation=evaluation
    )

    return response