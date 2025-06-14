# Step 1: Setup Streamlit UI (model provider, model, system prompt, online search, query)
# Run backend before running streamlit run code/frontend.py

import streamlit as st

# Configure Streamlit page
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("Personal AI Chatbot Agent")
st.write("Create and Interact with the AI Agents!")

# System prompt input box for user to define agent behavior
system_prompt = st.text_area("Define your AI Agent", height=70, placeholder="Type your system prompt here...")

# Define available models per provider
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

# Provider selection radio button
provider = st.radio("Select Provider:", ("Groq", "OpenAI"))

# Dynamically populate model options based on provider selection
if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

# Checkbox for enabling optional web search
allow_web_search = st.checkbox("Allow to search the web") 

# User query text area
user_query = st.text_area("Enter your Query", height=150, placeholder="Ask Anything!!!")

# Backend FastAPI server URL (make sure your FastAPI server is running)
API_URL = "http://127.0.0.1:9999/chat"

# Main interaction button
if st.button("Ask Agent!"):
    if user_query.strip():
        import requests

        # Prepare API payload matching FastAPI schema
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        # Send POST request to FastAPI backend
        response = requests.post(API_URL, json=payload)

        # Handle response from backend
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")
