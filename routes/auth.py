from fastapi import Depends, APIRouter, HTTPException, status, Form, Request, Response
from bleach import clean

from pydantic import ValidationError

from config.db import collection
from models.register import registerUser
from utils import get_password_hash, get_user


router = APIRouter(prefix="/v1/auth", tags=["authentication"])


@router.post("/register")
async def auth(
    req: Request,
    res: Response,
    email: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    password: str = Form(...),
):
    try:
        hashed_pass = get_password_hash(password)
        new_user = registerUser(
            first_name=clean(first_name),
            last_name=clean(last_name),
            email=email,
            password=hashed_pass,
        )
        if get_user(email):
            res.status_code = status.HTTP_400_BAD_REQUEST
            return {"message": "Email already registered"}
        else:
            collection.insert_one(new_user.dict())
            res.status_code = status.HTTP_201_CREATED
            return {"message": "User registered successfully"}

    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Validation Error! Please retry!",
        )
