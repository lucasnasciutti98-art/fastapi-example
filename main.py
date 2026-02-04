from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal
import bcrypt
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins= ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message":"welcome to my api!!!"}
