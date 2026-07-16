from fastapi import FastAPI
from app.models.schemas import UserQuery
from app.workflow.graph import run_workflow

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Credit Card Advisor API Running"}


@app.post("/recommend")
def recommend(data: UserQuery):
    result = run_workflow(data.query)
    return result