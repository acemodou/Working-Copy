from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/", description="This is our first route.", deprecated=True)
async def root():
    return {"message": "My name is Faraz, and Modou is a headache to manage"}

@app.post("/")
async def root():
    return {"message": "hello from the post route"}

@app.put("/")
async def root():
    return {"message": "hello from the put route"}

@app.get("/multiply")
async def multiply(a : int, b : int):
    return a * b

# @app.get("/items")
# async def list_items():
#     return {"message": "list items route"}

# @app.get("/items/{item_id}")
# async def get_items(item_id : int):
#     return {"item_id": item_id}

@app.get("/users/{user_id}")
async def get_user(user_id : str):
    return {"user_id": user_id}

@app.get("/users/me")
async def get_current_user():
    return {"Message": "This is a current user"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name : FoodEnum):
    if food_name == FoodEnum.fruits:
        return {"food_name": food_name, 
                "message" : "you are healthy"}

    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, 
                "message" : "you are still healthy, but like sweet things"}
    return {"food_name": food_name, "message": "I like chocolate milk"}

fake_item_db = [{"item_name" : "Foo"}, {"item_name" : "Bar"}, {"item_name" : "Baz"}]

@app.get("/items")
async def list_items(skip : int = 0, limit: int = 10):
    return fake_item_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def get_items(item_id : str, q : str | None = None, short: bool = False):
    items = {"item_id" : item_id}
    if q:
        items.update({"q" : q})
    if not short:
        items.update(
            {
                "description" : "blah blah"
            }
        )
    return items
 
class Item(BaseModel):
    name : str
    description : str | None = None 
    price : float 
    tax: float | None = None 

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.get("items")
async def read_items(
    q: str | None = Query(max_length = 10, min_length=3)
):
    results = [{"item_id": "Foo"}, {"item_id": "Bar"}]
    if q:
        results.update({"q": q})
    return results 

   