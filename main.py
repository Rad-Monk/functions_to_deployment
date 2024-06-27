import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from mylib.bot import scrape
from mylib.bot import add
from pydantic import BaseModel # basemodel makes it ys, basically allowing you to enforce data type

app = FastAPI()

class Wiki(BaseModel): # this defines what text you wanna send as a json payload from website
    name: str # this is the key for that json file and it's value should be string
    length: int

@app.post("/wiki")
async def scrape_story(wiki: Wiki):
    result = scrape(name=wiki.name, length=wiki.length)
    payload = {"wikipage": result}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/")
async def root():
    return {"message": "to use goto '/predict'"}

@app.get("/add/{num1}/{num2}")
async def add_nums(num1: int, num2: int):
    result = add(num1,num2)
    payload =  {"sum": f"{result} is the sum of {num1} and {num2}"}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

if __name__=="__main__":
    uvicorn.run(app,port=8081,host='0.0.0.0')