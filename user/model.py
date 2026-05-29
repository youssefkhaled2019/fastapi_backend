from sqlalchemy import Column, Integer, String,DateTime
from core.database import Base
from datetime import datetime
class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(  String,  unique=True,nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String,nullable=False)
    created_at = Column(    DateTime,   default=datetime.utcnow)
    #role = Column(String, default="user")