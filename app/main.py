from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.agent import build_answer

app = FastAPI(title="LLM Agent QA Demo", version="0.1.0")


class AnswerRequest(BaseModel):
    message: str = Field(description="User message for the agent")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/answer")
def answer(request: AnswerRequest) -> dict[str, str]:
    return build_answer(request.message)
