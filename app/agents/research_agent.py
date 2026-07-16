from langchain_core.prompts import ChatPromptTemplate

from app.services.llm import llm
from app.services.tavily_service import tavily_search


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are the Research Agent in a multi-agent credit card recommendation system.

Your ONLY responsibility is to research.

You receive:
- User spending profile
- User preferences
- Existing cards
- Web search results

Your task:

1. Read the web search results.
2. Extract factual information.
3. Organize the findings clearly.

DO NOT recommend cards.
DO NOT score cards.
DO NOT compare cards.
DO NOT make decisions.

Return only factual research.
"""
        ),
        ("human", "{query}")
    ]
)

chain = prompt | llm


def research_agent(requirement):

    search_query = f"""
Best Indian credit cards for the following profile:

Travel spend: ₹{requirement.travel}
Dining spend: ₹{requirement.dining}
Fuel spend: ₹{requirement.fuel}
Shopping spend: ₹{requirement.shopping}
Online spend: ₹{requirement.online}

Goal: {requirement.goal}

Current cards:
{", ".join(requirement.existing_cards) if requirement.existing_cards else "None"}

Find:

- Top matching credit cards
- Annual fee
- Joining fee
- Reward rates
- Cashback rates
- Lounge access
- Fuel benefits
- Dining benefits
- Welcome bonus
- Important eligibility
"""

    search_results = tavily_search(search_query)

    return chain.invoke(
        {
            "query": f"""
User Requirement

{requirement.model_dump()}

Web Search Results

{search_results}
"""
        }
    )