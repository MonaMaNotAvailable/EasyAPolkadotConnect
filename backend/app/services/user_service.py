from app.db.database import db_session
from app.models import User, CoffeeChatRequest

def register_user(user: User):
    db_session.execute(
        "INSERT INTO users (wallet_address, name, bio) VALUES (?, ?, ?)",
        (user.wallet_address, user.name, user.bio)
    )
    db_session.commit()
    return {"message": "User registered"}

def get_all_users():
    users = db_session.execute("SELECT wallet_address, name, bio FROM users").fetchall()
    return [dict(u) for u in users]

def create_chat_request(request: CoffeeChatRequest):
    db_session.execute(
        "INSERT INTO coffee_chats (requester_wallet, receiver_wallet, amount, accepted) VALUES (?, ?, ?, ?)",
        (request.requester_wallet, request.receiver_wallet, request.amount, False)
    )
    db_session.commit()

def accept_chat_request(request: CoffeeChatRequest):
    db_session.execute(
        "UPDATE coffee_chats SET accepted = 1 WHERE requester_wallet = ? AND receiver_wallet = ?",
        (request.requester_wallet, request.receiver_wallet)
    )
    db_session.commit()
