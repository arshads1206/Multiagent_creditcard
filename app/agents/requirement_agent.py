# requirement_agent.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from app.services.llm import llm
from app.models.schemas import Requirement

parser = JsonOutputParser(pydantic_object=Requirement)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert Credit Card Requirement Extraction Agent.

Extract the user's credit card requirements into JSON.

Extract:

- monthly_income
- monthly_spend
- dining
- shopping
- groceries
- fuel
- travel
- online
- utilities
- existing_cards
- goal
- annual_fee_preference
- lifestyle
- preferred_bank
- credit_score
- airport_lounge
- international_usage

Rules:

- Return ONLY valid JSON.
- Do not explain anything.
- If a spending category is not mentioned, use 0.
- If an enum value is not specified, use "Not Specified".
- existing_cards should always be a list.
- airport_lounge and international_usage should be true or false.
- monthly_income, monthly_spend and all spending fields must be integers.
- credit_score should be an integer. If unknown use 0.
"""
        ),
        ("human", "{query}")
    ]
)

chain = prompt | llm | parser


def requirement_agent(query: str):
    return chain.invoke(
        {
            "query": query,
            "format_instructions": parser.get_format_instructions()
        }
    )