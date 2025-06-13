# Step 1: setup API keys for Groq and Tavily and OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Step 2: Setup llm and tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

openai_llm=ChatOpenAI(model='gpt-4o-mini')
groq_llm=ChatGroq(model='llama-3.3-70b-versatile')

search_tool = TavilySearch(max_results=2)

# Step 3: Setup AI Agent with search tool functionality 
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt="Act as an AI chatbot which is smart"

# agent=create_react_agent(
#     model=groq_llm,
#     tools=[search_tool],
#     prompt=system_prompt  # This is for the agent role like analyst, stock broker
# )

# query="Tell me about the trends in crypto markets"
# state={"messages": query}
# response=agent.invoke(state)
# messages=response.get("messages")
# ai_message=[message.content for message in messages if isinstance(message, AIMessage)] 
# print(ai_message[-1])

# Given answer:
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


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider=="Groq":    
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)

    tools = [TavilySearch(max_results=2)] if allow_search else []

    agent=create_react_agent(
    model=llm,
    tools=tools,
    prompt=system_prompt  # This is for the agent role like analyst, stock broker
)

    state={"messages": query}
    response=agent.invoke(state)
    messages=response.get("messages")
    ai_message=[message.content for message in messages if isinstance(message, AIMessage)] 
    return ai_message[-1]