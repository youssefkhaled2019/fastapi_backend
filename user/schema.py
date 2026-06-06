from pydantic import BaseModel, EmailStr,Field,ConfigDict
from datetime import datetime
from typing import Optional



class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str= Field(min_length=8)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: int
    created_at: datetime
    role: str
    # class Config:
    #     from_attributes = True    
    model_config = ConfigDict(from_attributes=True)

class UserUpdatePatch(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class UserProfile(UserBase):

    id: int
    username: str
    email: EmailStr
    role: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
    # class Config:
    #     from_attributes = True                