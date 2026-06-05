from core.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer 
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException ,status
from user.model import User
from core.security import decode_token

oauth2_scheme = OAuth2PasswordBearer( tokenUrl="/auth/login")#request.headers.get("Authorization")



def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise        
    finally:
        db.close()

def get_current_user(  db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):

    payload = decode_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

   
    try:
        user_id = int(payload.get("sub"))
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Invalid token payload"
        )
    user = db.query(User).filter(  User.id == user_id).first()

    if not user:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user
    # return {"user_id": user_id}        



    
def get_current_admin(user: User = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
    return user

# def require_admin( user: User =Depends(get_current_user)):
#     if user.role != "admin":
#         raise HTTPException(
#             status_code=403,
#             detail="Not authorized"
#         )

#     return user
