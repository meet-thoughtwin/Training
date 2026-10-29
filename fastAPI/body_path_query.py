from fastapi import FastAPI
from pydantic import BaseModel

class Items(BaseModel):
    name:str
    descriptin: str | None=None
    price:float
    tax:float | None=None

app = FastAPI()

data =[]

@app.post("/itmes/")
async def create_item(items:Items):
    data.append(items)
    return {
        "message":"item created",
        "itme_data":items
    }


@app.get("/items/")
async def get_itmes():
    return {
        "data":data
    }

@app.put("/items/{item_id}")
async def update_item(itme_id:int, items:Items, q:str | None=None):
    result = {"itme_id":itme_id, "items":items}
    if q:
        result.update({"q":q})
    return result