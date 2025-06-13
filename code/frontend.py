# Step 1: Setup streamlit UI(model provder, model, system prompt, online search, query)

import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI", layout="wide")
st.title("Personal AI Chatbot Agent")
st.write("Create and Interact with the AI Agents!")

system_prompt=st.text_area("Define your AI Agent", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider=st.radio("Select Provider:", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search=st.checkbox("Allow to search the web") 

user_query=st.text_area("Enter your Query", height=150, placeholder="Ask Anything!!!")

if st.button("Ask Agent!"):
    if user_query.strip():
        # Get some backend respond.
        response = "Hi, I'm dummy"
        st.subheader("Agent Response")
        st.markdown(f"**Final Respnose:** {response}")
