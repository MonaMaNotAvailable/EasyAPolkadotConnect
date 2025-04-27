from pydantic import BaseModel as PydanticBaseModel
from typing import List, Optional
from datetime import datetime 
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from app.db.database import Base

# ------------------------
# Pydantic models (for API)
# ------------------------

class User(PydanticBaseModel):
    wallet_address: str
    name: str
    bio: Optional[str] = ""
    interests: Optional[List[str]] = []

class CoffeeChatRequest(PydanticBaseModel):
    requester_wallet: str
    receiver_wallet: str
    amount: float
    accepted: Optional[bool] = False

# ------------------------
# SQLAlchemy models (for DB)
# ------------------------

class TimeSlot(Base):
    __tablename__ = "timeslot"
    id = Column(Integer, primary_key=True, index=True)
    publisher_wallet = Column(String)
    datetime = Column(DateTime)
    betting_cap = Column(Float)  # Max bet allowed
    distribution_rule = Column(String)  # e.g., "return_to_winner", "use_for_coffee"
    is_open = Column(Boolean, default=True)

class Bet(Base):
    __tablename__ = "bet"
    id = Column(Integer, primary_key=True, index=True)
    time_slot_id = Column(Integer, ForeignKey('timeslot.id'))
    bidder_wallet = Column(String)
    amount = Column(Float)
    created_at = Column(DateTime)  # Add created_at for tiebreakers

class TimeSlotCreate(PydanticBaseModel):
    publisher_wallet: str
    datetime: datetime
    betting_cap: float
    distribution_rule: str

class BetCreate(PydanticBaseModel):
    bidder_wallet: str
    amount: float
