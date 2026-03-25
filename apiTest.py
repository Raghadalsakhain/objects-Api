from fastapi import FastAPI 
app = FastAPI()

items = []

@app.get("/objects")
def get_obgects():
    return items
@app.post("/objects")
def add_objects(item:dict):
    items.append(item)
    return{"message":"added"}