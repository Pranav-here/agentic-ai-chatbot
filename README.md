# LangGraph Agentic AI Chatbot

This project is a modular AI chatbot framework that allows dynamic interaction with multiple LLM providers using LangGraph, LangChain, Streamlit, and FastAPI. It also optionally integrates search tools such as Tavily for online augmentation.

The system consists of:

- Streamlit Frontend for user interaction
- FastAPI Backend to serve AI agent responses via REST API
- LangGraph-powered React Agent with support for Groq, OpenAI models, and Tavily search integration

## Features

- Dynamically select LLM Provider (Groq or OpenAI)
- Dynamically select available LLM models
- Optional web search augmentation using Tavily
- Custom system prompts per user session
- Stateless API endpoint for easy integration
- Fully interactive Streamlit user interface
- Modular backend logic via reusable agent creation functions

## Supported Models

- Groq: llama-3.3-70b-versatile, mixtral-8x7b-32768
- OpenAI: gpt-4o-mini

## Project Structure

| File/Folder      | Description                  |
|-------------------|------------------------------|
| `main.py`         | FastAPI Backend              |
| `frontend.py`     | Streamlit Frontend           |
| `ai_agent.py`     | Agent Creation Logic         |
| `backend.py`      | Pydantic Schema Validation   |
| `.env`            | Environment variables (API Keys) |
| `requirements.txt`| Python dependencies list     |
| `README.md`       | Project documentation        |
## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/langgraph-agentic-chatbot.git
cd langgraph-agentic-chatbot
```

2. **Setup virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Setup environment variables**

Create a `.env` file in the project root:

```bash
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

5. **Run Backend Server**

```bash
python backend.py
```

6. **Run Streamlit Frontend**

```bash
streamlit run frontend.py
```

7. **Test API (Swagger UI)**

Visit:

```
http://127.0.0.1:9999/docs
```

## Dependencies

- Python 3.10+
- LangChain
- LangGraph
- LangChain-Groq
- LangChain-OpenAI
- LangChain-Tavily
- FastAPI
- Pydantic
- Streamlit
- Uvicorn
- Requests
- python-dotenv

## Notes

- Make sure you have valid API keys for all providers you want to use.
- Tavily is optional and only used when web search is enabled.
- Backend and frontend communicate over HTTP (localhost).