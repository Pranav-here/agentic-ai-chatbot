# Step 1: Setup Pydantic Model(Schema Validation)

from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: list[str]
    allow_search: bool
