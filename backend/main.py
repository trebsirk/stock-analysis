from typing import Union

from cachetools import TTLCache, cached
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.stocks.stocks import get_stock_data

app = FastAPI()

origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cache = TTLCache(maxsize=1000, ttl=10)


@app.get("/")
async def index():
    return {"Hello": "World"}


@cached(cache)
@app.get("/stock/{ticker}")
async def get_stock(ticker: str):
    res = get_stock_data(ticker)
    return {"error getting stock {ticker}"} if res == {} else res
