from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router import post, users, auth, vote
from . import models
from .database import engine
from .config import settings

  
app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
    
app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)