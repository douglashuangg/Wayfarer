from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from keywords import *
from attraction import getAttraction

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
    item = item.text
    print(item)
    keywords = getKeyValues(item)
    sites = getAttraction(keywords)
    print(keywords)

    destinationResults = [keywords[0],sites, keywords[1]]
 
    return destinationResults
