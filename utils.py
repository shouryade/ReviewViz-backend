from jose import JWTError, jwt
from passlib.context import CryptContext
import os

context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def verify_hashed_password(plain_password, hashed_password):
    return context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return context.hash(password)
