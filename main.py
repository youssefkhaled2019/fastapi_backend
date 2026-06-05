from fastapi import FastAPI
from core.database import engine,Base
from user.router import router as user_router
from auth.router import router as auth_router
app = FastAPI(title="fastapi Project")


Base.metadata.create_all(bind=engine)


app.include_router(user_router)
app.include_router(auth_router)
@app.get("/")
def home():
    return {"message":"api v1"}

