from typing import Union

import users
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users")
def get_users():
    return [*users.get_users()]

@app.put("/users/{id}")
def update_user(id: int, user_data: User):
    print(user_data, id)
    user = users.update_user(id, user_data.name, user_data.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user