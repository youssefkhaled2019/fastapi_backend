from pydantic import BaseModel, EmailStr,ConfigDict
from pydantic import Field
from datetime import datetime

class RegisterCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=6)


class RegisterResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    role: str

    # class Config:
    #     from_attributes = True
    model_config = ConfigDict(from_attributes=True)


class LoginSchema(BaseModel):
    email: EmailStr
    password: str

    

class LoginTokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    # class Config:
    #     from_attributes = True
    model_config = ConfigDict(from_attributes=True)


class RefreshTokenRequest(BaseModel):
    refresh_token: str