from sqlalchemy.orm import Session
from user.model import User
from user.schema import UserCreate
from fastapi import HTTPException
def create_user(db: Session, user: UserCreate):
    db_user=db.query(User).filter(User.email == user.email).first()
    db_user=db.query(User).filter(User.username == user.username).first()
    if db_user or db_user:
         raise HTTPException(  status_code=400,  detail="Email or username already exists" )
    user_ = User(username=user.username, email=user.email,password=user.password)
    db.add(user_)
    db.commit()
    db.refresh(user_)
    return user_


def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, updated_data: UserCreate):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        try:
            user.username = updated_data.username
            user.email = updated_data.email
            user.password = updated_data.password
            db.commit()
            db.refresh(user)
        except:
             raise HTTPException(  status_code=400,  detail="Email or username already exists" )    
    return user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
       
    return user