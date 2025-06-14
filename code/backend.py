# Step 1: Setup Pydantic Model(Schema Validation)
# Run backend before running streamlit run code/frontend.py

from pydantic import BaseModel
from typing import List

# Define the request schema using Pydantic for type validation
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: list[str]  # User messages as list of strings
    allow_search: bool


# Step 2: Setup AI Agent at Frontend (API layer using FastAPI)
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent  # Function imported from your agent code

# Define allowed models to restrict invalid requests
ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192", 
    "mixtral-8x7b-32768", 
    "llama-3.3-70b-versatile", 
    "gpt-4o-mini"
]

# Initialize FastAPI app
app = FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the chatbot using LangGraph and search tools.
    Dynamically selects model and search tools based on request payload.
    """
    # Validate model name
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"Invalid Model name. Kindly select a valid model name"}

    # Extract fields from request payload
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Call agent function to get response
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response


# Step 3: Run app and Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)  # Swagger UI available at http://127.0.0.1:9999/docs
