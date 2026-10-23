from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []


# Request body model
class User(BaseModel):
    name: str
    age: int
    password: str


# Response model: password hide rahega
class UserResponse(BaseModel):
    name: str
    age: int


# POST API: Create user
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User created successfully"}


# GET API: Get users without password
@app.get("/users", response_model=list[UserResponse])
def get_users():
    return users
