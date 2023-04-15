from fastapi import Depends, APIRouter, HTTPException, status, Form, Request, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from bleach import clean
from datetime import datetime, timedelta
from typing import Annotated
import os

from pydantic import ValidationError

from config.db import collection
from models.register import registerUser
from utils import get_password_hash, verify_hashed_password


router = APIRouter(prefix="/v1/auth", tags=["authentication"])


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/register")
async def auth(
    req: Request,
    res: Response,
    email: str = Form(...),
    full_name: str = Form(...),
    password: str = Form(...),
):
    try:
        hashed_pass = get_password_hash(password)
        new_user = registerUser(
            full_name=clean(full_name),
            email=clean(email),
            password=hashed_pass,
        )
        if bool((collection.find_one({"email": email}))):
            res.status_code = 400
            return {"message": "Email already registered"}
        else:
            collection.insert_one(new_user.dict())
            res.status_code = 201
            return {"message": "User registered successfully"}

    except ValidationError:
        res.status_code = 422
        return {"message": "Validation error, please retry!"}
