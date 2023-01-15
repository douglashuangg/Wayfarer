from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from keywords import *
from server.attraction import getAttraction

keywords = []

class Input(BaseModel):
    text: str

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/save")
async def save_item(item: Input):
    print(item)
    keywords = getKeyValues(item)
    sites = getAttraction(keywords)
    print(keywords)
    return item

@app.get("/get-attraction")
async def root():
    return {"message": "Hello World"}