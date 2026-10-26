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

# from opentelemetry.semconv.attributes.http_attributes import HttpRequestMethodValues
# from fastapi import FastAPI, HTTPException, Depends, Header

# app = FastAPI()

# def verify_token(token:str = Header(None)):   # Header() is a part of an HTTP request that carries/stores additional information , such a authentication token,content type, or user agent
#     if token != "hello@meet1":
#         raise HTTPException(
#             status_code=401,
#             detail="unauthorized user"
#         )
#     return{
#         "message":"user authorized"
#     }

# @app.get("/user")
# def get_user(user= Depends(verify_token)):
#     return {
#         "message": "secure Data accessed",
#         "user":user
#     }


# ## example 3
# # we can use multiple dependencies in the single route 

# from fastapi import FastAPI, Depends, Header, HTTPException

# app = FastAPI()

# # Dependency 1:
# def verify_token(token: str = Header(None)):
#     if token != "hello@meet1":
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return "User authorized"


# # Dependency 2:
# def get_user_role():
#     return "admin"


# # Route function:
# @app.get("/user")
# def get_user(
#     user=Depends(verify_token),
#     role=Depends(get_user_role)
# ):
#     return {
#         "message": "Secure data accessed",
#         "user": user,
#         "role": role
#     }
