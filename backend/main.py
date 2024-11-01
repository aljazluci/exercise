import users
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import User


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # This only really works for development, should be changed if deploying
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

@app.get("/users")
def get_users(limit: int = 30):
    # Returns limit amount of users, or less if there are not enough in the "database"
    user_list = users.get_users(limit)
    if (not user_list) or (len(user_list) == 0):
        raise HTTPException(status_code=404, detail="No users retrieved")
    return [*users.get_users(limit)]

@app.put("/users/{id}")
def update_user(id: int, user_data: User):
    # updates user with given id, user_data can be incomplete, missing values are ignored
    user = users.update_user(id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user