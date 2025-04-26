from fastapi import APIRouter
from app.models import User, CoffeeChatRequest
from app.services import user_service, polkadot_service

router = APIRouter()

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
