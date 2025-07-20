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


# Frontend/
# Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
import streamlit as st
import requests

st.set_page_config(
    page_title="AI Agent using Langraph", page_icon=":robot_face:", layout="wide"
)
st.title("AI Agent")
st.write(
    "This is a simple AI Agent using Langraph. You can ask questions and get answers from the AI Agent. You can also search the web for information."
)

system_prompt = st.text_area(
    "Define your AI agent:",
    key="Enter your system prompt",
    placeholder="You are helpful AI chatbot assistant. You can answer questions and search the web for information.",
    height=70,
)

MODEL_NAME_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAME_OPENAI = ["gpt-4o-mini"]

provider = st.radio("select model provider", ["groq", "openai"], horizontal=True)

if provider == "groq":
    model_name = st.selectbox("select model", MODEL_NAME_GROQ)
else:
    model_name = st.selectbox("select model", MODEL_NAME_OPENAI)

allow_search = st.checkbox("Allow web search", value=True)

query = st.text_area(
    "Enter your query:", placeholder="Ask a question...", key="query_input", height=150
)

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Get Response"):
    if query.strip():
        with st.spinner("Getting response..."):
            payload = {
                "model_name": model_name,
                "messages": [query],
                "allow_search": allow_search,
                "system_prompt": system_prompt,
                "model_provider": provider,
            }
            response = requests.post(API_URL, json=payload)
            # response = (
            #     "Testing response from AI Agent"  # Placeholder for actual API call
            # )
            # st.subheader("Response from AI Agent:")
            # st.markdown(response)
            if response.status_code == 200:
                ai_response = response.json().get("response", "No response from AI.")
                st.success(ai_response)
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
    else:
        st.warning("Please enter a query.")

## Test.py file

{
    "messages": [
        HumanMessage(
            content="What is the latest news in India related to AI ",
            additional_kwargs={},
            response_metadata={},
            id="b9c97836-a04b-4dba-8f47-9871c8614a6a",
        ),
        AIMessage(
            content="",
            additional_kwargs={
                "tool_calls": [
                    {
                        "id": "call_g0bw",
                        "function": {
                            "arguments": '{"query":"latest news in AI"}',
                            "name": "tavily_search_results_json",
                        },
                        "type": "function",
                    }
                ]
            },
                       response_metadata={
                "token_usage": {
                    "completion_tokens": 53,
                    "prompt_tokens": 947,
                    "total_tokens": 1000,
                    "completion_time": 0.176793333,
                    "prompt_time": 0.032161947,
                    "queue_time": 0.050550013,
                    "total_time": 0.20895528,
                },
                "model_name": "llama3-70b-8192",
                "system_fingerprint": "fp_dd4ae1c591",
                "finish_reason": "tool_calls",
                "logprobs": None,
            },
            id="run--8183d2c6-39ca-4919-bd9d-53ffa0fe1876-0",
            tool_calls=[
                {
                    "name": "tavily_search_results_json",
                    "args": {"query": "latest news in AI"},
                    "id": "call_g0bw",
                    "type": "tool_call",
                }
            ],
                       usage_metadata={
                "input_tokens": 947,
                "output_tokens": 53,
                "total_tokens": 1000,
            },
        ),
        ToolMessage(
            content='[{"url": "https://www.crescendo.ai/news/latest-ai-news-and-updates", "content": "Summary: OpenAI launched \\"Operator,\\" a new AI assistant capable of handling various online tasks, such as ordering groceries and processing ticket purchases."}, {"url": "https://www.nbcnews.com/artificial-intelligence", "content": "The latest news and top stories on artificial intelligence, including AI chatbots like Microsoft\'s ChatGPT, Apple\'s AI Chatbot and Google\'s Bard."}]',
            name="tavily_search_results_json",
            id="e09dc2d6-c225-41fb-8604-a0c66ea9733e",
            tool_call_id="call_g0bw",
            artifact={
                "query": "latest news in AI",
                "follow_up_questions": None,
                "answer": None,
                "images": [],
                "results": [
                   {
                        "url": "https://www.crescendo.ai/news/latest-ai-news-and-updates",
                        "title": "Latest AI Breakthroughs and News: May-June 2025 - Crescendo.ai",
                        "content": 'Summary: OpenAI launched "Operator," a new AI assistant capable of handling various online tasks, such as ordering groceries and processing ticket purchases.',
                        "score": 0.7732339,
                        "raw_content": None,
                    },
                    {
                        "url": "https://www.nbcnews.com/artificial-intelligence",
                        "title": "Artificial intelligence - NBC News",
                        "content": "The latest news and top stories on artificial intelligence, including AI chatbots like Microsoft's ChatGPT, Apple's AI Chatbot and Google's Bard.",
                        "score": 0.769306,
                        "raw_content": None,
                    },
                ],
                               "response_time": 2.19,
            },
        ),
        AIMessage(
            content="According to the latest news, OpenAI has launched \"Operator\", a new AI assistant capable of handling various online, such as ordering groceries and processing ticket purchases. Additionally, there are ongoing developments in AI chatbots, with Microsoft's ChatGPT, and Google's Bard.",
            additional_kwargs={},
            response_metadata={
                "token_usage": {
                    "completion_tokens": 56,
                    "prompt_tokens": 1122,
                    "total_tokens": 1178,
                    "completion_time": 0.226801689,
                    "prompt_time": 0.038272468,
                    "queue_time": 0.064210402,
                    "total_time": 0.265074157,
                },
                "model_name": "llama3-70b-8192",
                "system_fingerprint": "fp_dd4ae1c591", 
                "finish_reason": "stop",
                "logprobs": None,
            },
            id="run--8183d2c6-39ca-4919-bd9d-53ffa0fe1876-1",
            tool_calls=None,
            usage_metadata={
                "input_tokens": 1122,
                "output_tokens": 56,
                "total_tokens": 1178,
            },
        ),
    ],
    "response_metadata": {
        "model_name": "llama3-70b-8192",
        "system_fingerprint": "fp_dd4ae1c591",
        "finish_reason": "stop",
        "token_usage": {
            "completion_tokens": 56,
            "prompt_tokens": 1122,
            "total_tokens": 1178,
            "completion_time": 0.226801689,
            "prompt_time": 0.038272468,
            "queue_time": 0.064210402,
            "total_time": 0.265074157,
        },
    },