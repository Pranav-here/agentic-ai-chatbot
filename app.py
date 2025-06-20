# STEP 1: Load environment variables and retrieve API keys
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env file in the project root

GROQ_API_KEY  = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# STEP 2: Import LLM wrappers and optional web‑search tool
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

# STEP 3: Helper to build a fresh agent and return its reply

def get_response_from_ai_agent(
    model_name: str,
    query: str,
    allow_search: bool,
    system_prompt: str,
    provider: str,
) -> str:
    """Return the assistant's reply for *query*.

    Args:
        model_name: ID string understood by the chosen provider.
        query: User prompt.
        allow_search: Toggles Tavily web search (max‑2 results).
        system_prompt: System instructions injected before conversation.
        provider: "Groq" or "OpenAI".

    Returns:
        Assistant message as plain text.
    """
    # Select backend LLM
    llm = ChatGroq(model=model_name) if provider == "Groq" else ChatOpenAI(model=model_name)

    # Attach tools only when requested
    tools = [TavilySearch(max_results=2)] if allow_search else []

    # Build one‑shot reactive agent
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt or "You are a helpful AI assistant."
    )

    # LangGraph expects the conversation stored under "messages"
    state = {"messages": query}

    # Run the agent graph
    out = agent.invoke(state)
    msgs = out.get("messages", [])
    ai_msgs = [m.content for m in msgs if isinstance(m, AIMessage)]

    return ai_msgs[-1] if ai_msgs else "No response generated."

# STEP 4: Streamlit UI: collect user inputs & display the answer
import streamlit as st

st.set_page_config(page_title="Agentic AI Chatbot", layout="wide")
st.title("Agentic AI Chatbot")
st.caption("Single‑file Streamlit interface powered by LangGraph agents")

#  Sidebar: configuration
with st.sidebar:
    st.header("Settings")
    system_prompt = st.text_area(
        "System prompt",
        height=80,
        placeholder="Act as a data‑savvy analyst",
    )
    allow_search = st.checkbox("Enable Tavily Web Search")

# Provider & model selection
col1, col2 = st.columns(2)
with col1:
    provider = st.selectbox("Provider", ("OpenAI", "Groq"))
with col2:
    model = st.selectbox(
        "Model",
        (
            "gpt-4o-mini",
            "gpt-4.1",
            "o4-mini"
        ) if provider == "OpenAI" else (
            "gemma2-9b-it",
            "llama-3.3-70b-versatile",
            "qwen-qwq-32b",
        )
    )

#  Main chat input 
query = st.text_area("Your question", height=100)

if st.button("Run Agent"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Thinking..."):
            answer = get_response_from_ai_agent(
                model_name=model,
                query=query,
                allow_search=allow_search,
                system_prompt=system_prompt,
                provider=provider,
            )
        st.markdown("### Response")
        st.write(answer)
