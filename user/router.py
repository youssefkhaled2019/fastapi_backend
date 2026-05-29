from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session

from core.dependencies import get_db
from user.schema import UserCreate, UserResponse
import user.service as service

router = APIRouter(prefix="/users", tags=["Users"])



@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)


@router.get("/", response_model=list[UserResponse])
def read_all(db: Session = Depends(get_db)):
    return service.get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def read_one(user_id: int, db: Session = Depends(get_db)):
    return service.get_user(db, user_id)


@router.put("/{user_id}", response_model=UserResponse)
def update(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return service.update_user(db, user_id, user)


@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    if service.delete_user(db, user_id):
        return {"message": "User deleted successfully"}

    raise HTTPException(status_code=404, detail="User not found")

