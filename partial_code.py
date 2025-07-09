##Backend

# Step1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from agent import get_response_from_ai_agent
import uvicorn


class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


# Step2: Setup AI Agent from FrontEnd Request
app = FastAPI(title="LangGraph AI Agent")
ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768",
    "llama-3.3-70b-versatile",
    "gpt-4o-mini",
]


@app.post("/chat")
def chat(request_state: RequestState):
    """
    This endpoint receives a chat request with the model name, provider, system prompt, and messages.
    It processes the request and returns a response from the AI agent.
    """
    if request_state.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Model not allowed"}

    llm_id = request_state.model_name
    provider = request_state.model_provider
    prompt = request_state.system_prompt
    query = request_state.messages
    allow_search = request_state.allow_search

    # Create AI Agent and get response from it!
    response = get_response_from_ai_agent(llm_id, query, allow_search, prompt, provider)
    return {"response": response}


# Step3: Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9999)
