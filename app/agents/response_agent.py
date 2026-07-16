# response_agent.py
from langchain_core.prompts import ChatPromptTemplate

from app.services.llm import llm

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are the Final Credit Card Advisor.

You receive the evaluation results from another AI agent.

Your responsibility is to generate a professional recommendation.

Rules:

- Recommend ONLY one best card.
- Explain WHY it is the best choice.
- Mention the estimated yearly rewards/savings.
- Mention one alternative option.
- Mention who the recommendation is best suited for.
- Give a confidence score out of 100.
- Keep the response concise and professional.
- Do NOT invent information.
- Only use the evaluation provided.
"""
        ),
        (
            "human",
            """
User Requirement

{requirement}


Evaluation

{evaluation}
"""
        )
    ]
)

chain = prompt | llm


def response_agent(requirement, evaluation):

    return chain.invoke(
        {
            "requirement": requirement,
            "evaluation": evaluation
        }
    )