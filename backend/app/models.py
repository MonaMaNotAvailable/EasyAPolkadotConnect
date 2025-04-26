from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    wallet_address: str
    name: str
    bio: Optional[str] = ""
    interests: Optional[List[str]] = []

class CoffeeChatRequest(BaseModel):
    requester_wallet: str
    receiver_wallet: str
    amount: float  # e.g., 0.01 DOT
    accepted: Optional[bool] = False
