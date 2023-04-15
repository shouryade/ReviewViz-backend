from pydantic import BaseModel
from fastapi import Form


class registerUser(BaseModel):
    full_name: str = Form(...)
    email: str = Form(...)
    password: str = Form(...)
