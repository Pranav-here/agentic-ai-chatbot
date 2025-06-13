# Step 1: setup API keys for Groq and Tavily and OpenAI
import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Step 2: Setup llm and tools
from langchain_groq import chat_groq
from langchain_openai import ChatOpenAI
from langchain_community.tools import TavilySearchResults

openai_llm=ChatOpenAI(model='gpt-4o-mini')
groq_llm=chat_groq(model='llama-3.3-70b-versatile')

search_tool = TavilySearchResults(max_results=2)  # 

# Step 3: Setup AI Agent with search tool functionality 

system_prompt="Act as an AI chatbot which is smart"

from langgraph.prebuilt import creat_react_agent
agent=creat_react_agent(
    model=groq_llm,
    tools=[search_tool],
    state_modifier=system_prompt  # This is for the agent role like analyst, stock broker
)

query="Tell me about the trends in crypto markets"
state={"messages": query}
response=agent.invoke(state)
print()
