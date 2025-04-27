from fastapi import FastAPI
from app.routes import router
from app.db.database import Base, engine

app = FastAPI(title="EasyAPolkadotCoffeeChat Backend")

# include your API routes
app.include_router(router)

# create all tables when server starts
@app.on_event("startup")
async def startup_event():
    # import models so they are registered properly
    from app import models
    Base.metadata.create_all(bind=engine)

# root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to EasyAPolkadotCoffeeChat!"}