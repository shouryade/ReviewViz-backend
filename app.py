from fastapi import FastAPI
import uvicorn
from db import db

app = FastAPI()
from routes import auth
from dotenv import load_dotenv
import os

load_dotenv()

app.include_router(auth.router)


MONGODB_CONNECTION_URI = os.getenv("MONGODB_CONNECTION_URI")


@app.on_event("startup")
async def startup():
    db.connect_to_database(MONGODB_CONNECTION_URI)


@app.get("/")
async def hello():
    msg = db.ping()
    return {"msg": msg}


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, host="127.0.0.1", port=8000)
