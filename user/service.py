from sqlalchemy.orm import Session
from user.model import User
from user.schema import UserCreate,UserUpdatePatch
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from core.security import hash_password
from sqlalchemy import or_
from core.logger import logger
def create_user(db: Session, user: UserCreate):
    #db_user=db.query(User).filter(  (User.email == user.email) | (User.username == user.username)).first()
    db_user = db.query( User).filter( or_( User.email == user.email,User.username == user.username ) ).first()
    if db_user :
         raise HTTPException(  status_code=400,  detail="Email or username already exists" )
    try:
        user_ = User(username=user.username, email=user.email,password=hash_password(user.password))
        db.add(user_)
        db.commit()
        db.refresh(user_)
        logger.info( f"User create: {user_.id}"+" info_2026_4")
        return user_
    except IntegrityError:
        db.rollback()
        raise HTTPException(  status_code=400,detail="error - create_user ")


# def get_users(db: Session):
#     return db.query(User).all()

def get_users(db: Session,skip: int = 0, limit: int = 10,search: str | None = None):
    # return db.query(User).offset(skip).limit(limit).all()
    query = db.query(User)
    if search:
        query = query.filter(or_(User.username.ilike(f"%{search}%"),User.email.ilike(f"%{search}%")))
    return query.offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(    status_code=404,  detail="User not found")

    return user

def update_user(db: Session, user_id: int, updated_data: UserCreate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(  status_code=400,  detail="user not  exist" )    # return None
    
    user_existing = db.query(User).filter(    (User.email == updated_data.email) | (User.username == updated_data.username), User.id != user_id).first() 
    if user_existing:
        raise HTTPException( status_code=400,detail="Email or username already exists" )
   
    try:
        user.username = updated_data.username
        user.email = updated_data.email
        user.password = hash_password(updated_data.password)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise HTTPException(  status_code=400,detail="error - update_user ")
    
def update_user_patch(db: Session, user_id: int, updated_data: UserUpdatePatch):

    user = db.query(User).filter(User.id == user_id).first() 
    if not user:
        raise HTTPException(  status_code=400,  detail="user not  exist" )    # return None
    
    user_existing = db.query(User).filter(    (User.email == updated_data.email) | (User.username == updated_data.username), User.id != user_id).first() 
    if user_existing:
        raise HTTPException( status_code=400,detail="Email or username already exists" )


    try:
        data = updated_data.model_dump(exclude_unset=True)
        for key, value in data.items():
            if key == "password" and value:
                value = hash_password(value) 
            setattr(user, key, value)
        db.commit()
        db.refresh(user)    
        return user
    except IntegrityError:
        db.rollback()
        raise HTTPException(  status_code=400,detail="error - update_user_patch ")
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
       raise HTTPException(status_code=404, detail="User not found")

    try:
        db.delete(user)
        db.commit()
        logger.info( f"User deleted: {user_id}"+" info_2026_3")
        return {"message": "User deleted successfully"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(  status_code=400,detail="error - delete_user ")