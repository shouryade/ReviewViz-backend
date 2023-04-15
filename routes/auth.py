from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from bleach import clean
from pymongo import MongoClient
from datetime import datetime, timedelta
from typing import Annotated
import os

from pydantic import BaseModel

router = APIRouter(prefix="/v1/auth", tags=["authentication"])

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


@router.get("/register")
async def auth():
    return {"msg": SECRET_KEY}
