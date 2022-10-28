from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import (Users)
from routes.code import Code
from routes.login import Login
from routes.post import Posts

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(Users.router)
app.include_router(Posts.router)
app.include_router(Login.router)
app.include_router(Code.router)
