from fastapi import APIRouter, Depends
from auth.schema import RegisterResponse,RegisterCreate,LoginSchema,LoginTokenResponse
from sqlalchemy.orm import Session
from core.dependencies import get_db
from auth import service

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=RegisterResponse)
def register(user: RegisterCreate,db: Session = Depends(get_db)):
   return service.register_user(user,db)

@router.post("/login",response_model=LoginTokenResponse)
def login(user:LoginSchema,   db: Session = Depends(get_db)):
   return service.login(user,db)



