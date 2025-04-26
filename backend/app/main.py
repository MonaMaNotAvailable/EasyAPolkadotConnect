from fastapi import FastAPI
from app.routes import router
from app.db.database import create_tables

app = FastAPI(title="EasyAPolkadotCoffeeChat Backend")

app.include_router(router)

# create tables when server starts
@app.on_event("startup")
async def startup_event():
    create_tables()

# Define a root endpoint to handle requests to '/'
@app.get("/")
def read_root():
    return {"message": "Welcome to EasyAPolkadotCoffeeChat!"}