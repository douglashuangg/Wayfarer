from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from keywords import *


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

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/save")
async def save_item(item: Input):
    print(item)
    keywords = getKeyValues(item)
    print(keywords)
    destinationResults = [
    {
        "name": "CN Tower",
        "price": 1000,
        "description": "Cn Tower is 500 m tall.",
        "url": "https fake"
    },
    {
        "name": "ROM",
        "price": 2000,
        "description": "ROM is cool.",
        "url": "https fake"
    },
    {
        "name": "Centre Island",
        "price": 20000,
        "description": "Water surrounds it",
        "url": "https fake"
    },
    {
        "name": "Casa de Loma",
        "price": 500,
        "description": "Go big or go home",
        "url": "https fake"
    },
    ]
    return destinationResults