from app.db.database import get_db
from app.models import User, CoffeeChatRequest
from sqlalchemy.orm import Session

# Register a user
def register_user(user: User, db: Session):
    db.execute(
        "INSERT INTO users (wallet_address, name, bio) VALUES (?, ?, ?)",
        (user.wallet_address, user.name, user.bio)
    )
    db.commit()
    return {"message": "User registered"}

# Get all users
def get_all_users(db: Session):
    users = db.execute("SELECT wallet_address, name, bio FROM users").fetchall()
    return [dict(u) for u in users]

# Create a coffee chat request
def create_chat_request(request: CoffeeChatRequest, db: Session):
    db.execute(
        "INSERT INTO coffee_chats (requester_wallet, receiver_wallet, amount, accepted) VALUES (?, ?, ?, ?)",
        (request.requester_wallet, request.receiver_wallet, request.amount, False)
    )
    db.commit()

# Accept a coffee chat request
def accept_chat_request(request: CoffeeChatRequest, db: Session):
    db.execute(
        "UPDATE coffee_chats SET accepted = 1 WHERE requester_wallet = ? AND receiver_wallet = ?",
        (request.requester_wallet, request.receiver_wallet)
    )
    db.commit()
