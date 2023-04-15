from pydantic import BaseModel
from fastapi import Form


class registerUser(BaseModel):
    username: str = Form(...)
    email: str | None = Form(...)
    phone: int | None = Form(...)
    full_name: str | None = Form(...)
