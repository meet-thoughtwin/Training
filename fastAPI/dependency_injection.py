## example 1

# from fastapi import FastAPI, Depends

# app = FastAPI()

# def common_function():
#     return {
#         "message": "hello user"
#     }

# @app.get("/user")
# def user(data: dict = Depends(common_function)):
#     return data


## example 2


from opentelemetry.semconv.attributes.http_attributes import HttpRequestMethodValues
from fastapi import FastAPI, HTTPException, Depends, Header

app = FastAPI()

def verify_token(token:str = Header(None)):
    if token != "hello@meet1":
        raise HTTPException(
            status_code=401,
            detail="unauthorized user"
        )
    return{
        "message":"user authorized"
    }

@app.get("/user")
def get_user(user= Depends(verify_token)):
    return {
        "message": "secure Data accessed",
        "user":user
    }


