from fastapi import FastAPI # import fastapi class from the fastapi package

app = FastAPI() # initializing fastapi as object

@app.get("/") # defining a route for GET request
def user(): # function to handle the GET request
    return {
        "message":"hello users"
    }

@app.get("/user/{user_id}")  # path parameter define in both in route and in function's argument
def get_user(user_id: int = None): # we also apply validation here by specifying int type
    return {
        "user_id":user_id
    }

@app.get("/product/{product_id}")
def get_product(product_id: int = None, limit: int = 10, product: str = "not found"):
    return {
        "product_id": product_id,
        "limit": limit,
        "product":product
    }