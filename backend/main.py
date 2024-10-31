from typing import Union

import users
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users")
def get_users():
    return [*users.get_users()]

@app.put("/users/{id}")
def update_user(id, name=None, email=None):
    user = users.update_user(id, name, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user