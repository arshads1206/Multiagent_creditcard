# evaluation_agent.py
from langchain_core.prompts import ChatPromptTemplate

from app.services.llm import llm

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Credit Card Evaluation Agent.

You are NOT allowed to recommend a card.

Your ONLY job is to evaluate every researched credit card objectively.

Evaluate each card using:

- Dining benefits
- Shopping rewards
- Travel rewards
- Fuel benefits
- Airport lounge access
- Annual fee
- Joining bonus
- Reward rate
- Existing cards owned by the user
- Lifestyle match

For every card produce:

Name

Score (0-100)

Pros

Cons

Estimated yearly reward potential

Return structured markdown.
"""
        ),
        (
            "human",
            """
User Requirement

{requirement}


Research

{research}
"""
        )
    ]
)

chain = prompt | llm


def evaluation_agent(requirement, research):

    return chain.invoke(
        {
            "requirement": requirement,
            "research": research
        }
    )