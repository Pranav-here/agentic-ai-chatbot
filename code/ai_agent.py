# Step 1: setup API keys for Groq and Tavily and OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Step 2: Setup llm and tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

# Initialize LLM clients with default models
openai_llm = ChatOpenAI(model='gpt-4o-mini')
groq_llm = ChatGroq(model='llama-3.3-70b-versatile')

# Setup optional web search tool using Tavily (limit to 2 results)
search_tool = TavilySearch(max_results=2)

# Step 3: Setup AI Agent with search tool functionality 
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

# Define the system prompt to control agent behavior
system_prompt = "Act as an AI chatbot which is smart"

# Example agent setup (currently commented out for modular use)
# agent=create_react_agent(
#     model=groq_llm,
#     tools=[search_tool],
#     prompt=system_prompt  # This is for the agent role like analyst, stock broker
# )

# Example query for testing (currently commented out)
# query="Tell me about the trends in crypto markets"
# state={"messages": query}
# response=agent.invoke(state)
# messages=response.get("messages")
# ai_message=[message.content for message in messages if isinstance(message, AIMessage)] 
# print(ai_message[-1])

# Given answer (example output from agent)
"""
    Based on the search results, the current trends in crypto markets are not explicitly stated. 
    However, the search results provide links to websites that offer real-time prices, changes, 
    trading volume, and daily charts for various cryptocurrencies. These resources can be used to 
    stay up-to-date with the latest developments in the crypto market.

    To get a better understanding of the current trends, you can visit the websites provided in 
    the search results, such as Yahoo Finance's crypto page, which offers a comprehensive list of 
    cryptocurrencies with their current prices, percentage changes, volume, open interest, and 
    daily charts.
"""

# Utility function to generate AI agent response dynamically
def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    """
    Generate a response from AI agent based on given parameters.

    Args:
        llm_id (str): The model ID to be used (e.g. 'gpt-4o-mini', 'llama-3.3-70b-versatile').
        query (str): User's input query.
        allow_search (bool): Whether to enable Tavily web search.
        system_prompt (str): Custom system instructions for agent behavior.
        provider (str): Which provider to use ("Groq" or "OpenAI").

    Returns:
        str: The generated response from the AI agent.
    """
    # Dynamically select LLM based on provider
    if provider == "Groq":    
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)

    # Enable tools if search is allowed
    tools = [TavilySearch(max_results=2)] if allow_search else []

    # Create reactive agent using LangGraph
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt  # This is for the agent role like analyst, stock broker
    )

    # Prepare agent state (LangGraph expects messages dict)
    state = {"messages": query}

    # Invoke agent to generate response
    response = agent.invoke(state)

    # Extract messages and filter for AI-generated content
    messages = response.get("messages")
    ai_message = [message.content for message in messages if isinstance(message, AIMessage)] 
    
    return ai_message[-1]