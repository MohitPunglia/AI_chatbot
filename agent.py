# Step1: Setup API Keys for Groq, OpenAI and Tavily
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Step2: Setup LLM & Tools
openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama3-70b-8192")


# Step3: Setup Agent

prompt = "You are helpful AI chatbot assitant. You can answer questions and search the web for information."


def get_response_from_ai_agent(llm_id, query, allow_search, prompt, provider):
    if provider == "groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "openai":
        llm = ChatOpenAI(model=llm_id)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(model=llm, tools=tools, state_modifier=prompt)

    # query = "Who won the IPL 2025"

    state = {"messages": query}

    response = agent.invoke(state)

    messages = response.get("messages")
    ai_messages = [
        message.content for message in messages if isinstance(message, AIMessage)
    ]
    return ai_messages[-1]
