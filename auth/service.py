from sqlalchemy.orm import Session
from user.model import User
from fastapi import HTTPException
from sqlalchemy import or_
from core import security
from user.service import create_user
# -----
from core.security import decode_token, create_access_token
def register_user(user,db: Session):
    # db_user = db.query( User).filter( or_( User.email == user.email,User.username == user.username ) ).first()
    # if db_user:
    #     if db_user.email == user.email:
    #         raise HTTPException(  status_code=400,  detail="Email already exists" )
    #     if db_user.username == user.username:
    #         raise HTTPException(status_code=400, detail="Username already exists" )
    # hashed_password = security.hash_password( user.password)
    # new_user = User( username=user.username, email=user.email,password=hashed_password)
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)

    new_user=create_user(db,user)

    return new_user



def login(user,   db: Session):

    db_user = db.query( User).filter(User.email == user.email ).first()
    if not db_user:
        raise HTTPException(status_code=400,detail="Invalid credentials")

    valid_password = security.verify_password(user.password,db_user.password)

    if not valid_password:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = security.create_access_token( data={"sub":  str(db_user.id), "role": db_user.role}) #{"sub": str(user.id),  "role": user.role}
    refresh_token = security.create_refresh_token( {     "sub": str(db_user.id) }
)
    if not access_token:
        raise HTTPException( status_code=401, detail="Invalid credentials")
        # return None
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }




def refresh_access_token(refresh_token: str):

    payload = decode_token(refresh_token)

    if payload.get("type") != "refresh":
        raise HTTPException(      status_code=401,        detail="Invalid refresh token"    )

    user_id = payload.get("sub")

    access_token = create_access_token({"sub": user_id,  } )

    return {  "access_token": access_token,    "token_type": "bearer"  }