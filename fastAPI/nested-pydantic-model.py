from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data=[]

class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    id:int
    name:str
    details:Address

@app.post("/user")
def user_creation(user:User):
    data.append(user)
    return {
        "message":"user created",
        "data":user
    }

@app.get("/user")
def get_users():
    return data


@app.get("/user/{user_id}")
def get_user(user_id:int):
    for item in data:
        if item.id == user_id:
            return item
    return{"error":"data not found"}

@app.delete("/user/{user_id}")
def delete_user(user_id:int):
    for index , item in enumerate(data):
        if item.id == user_id:
            data.pop(index)
            return{"message":"data deleted"}
    return {"error":"data not found"}