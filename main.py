from fastapi import FastAPI
from core.database import engine,Base
from user.router import router as user_router

app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(user_router)

@app.get("/")
def home():
    return {"message":"api v1"}

