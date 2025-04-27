from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import User, CoffeeChatRequest
from app import crud, models
from app.db.database import get_db
from app.services import user_service, polkadot_service

router = APIRouter()

# ----------------------------------
# User-related routes
# ----------------------------------

@router.post("/register")
def register_user(user: User):
    return user_service.register_user(user)

@router.get("/browse")
def browse_users():
    return user_service.get_all_users()

@router.post("/request-chat")
def request_chat(request: CoffeeChatRequest):
    tx_hash = polkadot_service.send_payment(
        from_wallet=request.requester_wallet,
        to_wallet=request.receiver_wallet,
        amount=request.amount
    )
    user_service.create_chat_request(request)
    return {"message": "Chat request sent", "tx_hash": tx_hash}

@router.post("/accept-chat")
def accept_chat(request: CoffeeChatRequest):
    tx_hash = polkadot_service.refund_payment(
        from_wallet=request.receiver_wallet,
        to_wallet=request.requester_wallet,
        amount=request.amount
    )
    user_service.accept_chat_request(request)
    return {"message": "Chat accepted and refunded", "tx_hash": tx_hash}

# ----------------------------------
# TimeSlot and Bet
# ----------------------------------

# Create a time slot for betting
@router.post("/time-slot/")
def create_time_slot(slot_data: models.TimeSlotCreate, db: Session = Depends(get_db)):
    return crud.create_time_slot(db, slot_data)

# Place a bet on a specific time slot
@router.post("/time-slot/{time_slot_id}/bet")
def place_bet(time_slot_id: int, bet_data: models.BetCreate, db: Session = Depends(get_db)):
    return crud.place_bet(db, time_slot_id, bet_data)

# Close the time slot and pick winner
@router.post("/time-slot/{time_slot_id}/close")
def close_time_slot(time_slot_id: int, db: Session = Depends(get_db)):
    return crud.close_time_slot(db, time_slot_id)
