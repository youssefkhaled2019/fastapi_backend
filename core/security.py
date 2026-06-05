from passlib.context import CryptContext


from fastapi import HTTPException
from jose import jwt, JWTError
from datetime import datetime, timedelta

from core.config import settings


# SECRET_KEY = settings.SECRET_KEY
ALGORITHM =settings.ALGORITHM #"HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext( schemes=["bcrypt"],deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)
def verify_password( plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password,hashed_password)



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(  to_encode, settings.SECRET_KEY,    algorithm=ALGORITHM   )

def decode_token(token: str):#
    try:
        payload = jwt.decode( token, settings.SECRET_KEY, algorithms=[ALGORITHM] )
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail=" JWTError " )