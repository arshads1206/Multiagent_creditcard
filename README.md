# Multi-Agent Credit Card Advisor

An AI-powered, multi-agent system designed to analyze user spending habits and preferences to recommend the most suitable credit cards.

## Features

- **Requirement Extraction**: Automatically extracts income, spending categories (dining, travel, etc.), and preferences from natural language queries.
- **Agentic Workflow**:
  - **Requirement Agent**: Parses user input into a structured format.
  - **Research Agent**: Gathers information about relevant credit cards.
  - **Evaluation Agent**: Analyzes cards based on user requirements and potential rewards.
  - **Response Agent**: Crafts a personalized, easy-to-understand recommendation.
- **FastAPI Backend**: Exposes a clean REST API for generating recommendations.

## Tech Stack

- **Python 3.x**
- **FastAPI**
- **LangChain**
- **Pydantic** for structured data modeling

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/arshads1206/Multiagent_creditcard.git
   cd Multiagent_creditcard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in `.env` (use the provided `.env.example` if available, or specify the following keys):
   ```env
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

## Usage

Start the FastAPI development server:
```bash
uvicorn app.main:app --reload
```

### API Endpoints

- `GET /` : Health check.
- `POST /recommend`: Submits a user query for credit card recommendation.
  ```json
  {
    "query": "I earn $5000 a month and spend a lot on travel and dining. Recommend a card with good lounge access."
  }
  ```

## Structure

- `app/main.py`: FastAPI application entry point.
- `app/agents/`: Logic for the various agents in the workflow.
- `app/workflow/graph.py`: Coordinates the agents.
- `app/services/`: LLM and search tool integrations.
- `app/models/`: Pydantic schemas for structured data.
