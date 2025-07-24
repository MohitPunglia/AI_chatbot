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
