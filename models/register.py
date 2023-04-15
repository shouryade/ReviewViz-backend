from pydantic import BaseModel
from fastapi import Form


class registerUser(BaseModel):
    full_name: str = Form(...)
    username: str = Form(...)
    phone: int = Form(...)
    email: str = Form(...)
    password: str = Form(...)
