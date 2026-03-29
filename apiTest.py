from fastapi import FastAPI, Request, HTTPException, Depends
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()
items = []

API_KEY = os.getenv("API_KEY")

def check_api_key(request:Request):
    api_key = request.headers.get("x-api-key")
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
##privet 
@app.get("/objects")
def get_items(dep=Depends(check_api_key)):
    return items

##path parameter {} 
@app.get("/objects/{item_id}")
def get_objectsbyID(item_ID:int, Depends(check_api_key)):
    for item in items:
        if item["id"]==item_ID:
         return item
    return {"error":"not found"}

@app.post("/objects")
def add_item(item: dict, dep=Depends(check_api_key)):
    item["id"] = len(items) + 1
    items.append(item)
    return {"message": "added"}


@app.put("/objects/{item_id}")
def update_object(item_ID:int, item_update:dict,dep=Depends(check_api_key)):
       for item in items:
          if item["id"]==item_ID:
             items[items.index(item)]=item_update
             return {"message":"update is done"}
          return {"error":"not found"}
       
   
@app.patch("/objects/{item_id}")
def update_object(item_ID:int, item_update:dict ,dep=Depends(check_api_key)):
   for item in items:
      if item["id"]==item_ID:
        item.update(item_update)
        return item 
      return {"error":"not found"}


@app.delete("/objects/{item_id}")
def update_object(item_id:int, dep=Depends(check_api_key)):
   for item in items:
      if item["id"]==item_id:
         items.remove(item)
         return {"message":"remove is done"}
      return {"error":"not found"} 
   


   ##public 

@app.get("/objects")
def get_obgects():
    result=[]
    for item in items :
       new_item={"id":item["id"], "name":item["name"]}
       result.append(new_item)

    return result

@app.get("/objects/{item_id}")
def get_objectsbyID(item_ID:int):
    for item in items:
        if item[id]==item_ID:
         return item["id"],item["name"]
    return {"error":"not found"}

# @app.post("/objects")
# def add_objects(item:dict):
#     item["id"] =len(items)+1
#     items.append(item)
#     return{"message":"added"}


# @app.put("/objects/{item_id}")
# def update_object(item_ID:int , item_updated:dict):
#    for item in items:
#       if item[id]==item_ID:
#         items[items.index(item)]=item_updated
#         return {"message":"update is done"}
#    return {"error":"not fount"}


# @app.patch("/objects/{item_id}")
# def update_object(item_ID:int, item_update:dict):
#    for item in items:
#       if item[id]==item_ID:
#        item.update(item_update)
#        return items
#    return {"message":"not found"}


# @app.delete("/objects/{item_id}")
# def delete_object(item_ID:int, item_delete:dict):
#    for item in items:
#       if item[id]==item_ID:
#          items.remove(item)
#          return {"message":"deleted is done"}
#       return {"error":"not found"}

