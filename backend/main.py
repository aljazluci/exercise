from typing import Union

import users
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class User(BaseModel):
    name: str | None = None
    email: str | None = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change this to your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/users")
def get_users(limit: int = 30):
    return [*users.get_users(limit)]

@app.put("/users/{id}")
def update_user(id: int, user_data: User):
    user = users.update_user(id, user_data.name, user_data.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user