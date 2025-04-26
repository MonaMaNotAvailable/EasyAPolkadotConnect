import sqlite3

db_session = sqlite3.connect("coffeechat.db", check_same_thread=False)

def create_tables():
    cursor = db_session.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wallet_address TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            bio TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS coffee_chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            requester_wallet TEXT NOT NULL,
            receiver_wallet TEXT NOT NULL,
            amount REAL NOT NULL,
            accepted BOOLEAN DEFAULT FALSE
        )
    """)
    db_session.commit()
