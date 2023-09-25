from typing import Union

from cachetools import TTLCache, cached
from fastapi import FastAPI

from backend.stocks.stocks import get_stock_data

app = FastAPI()

cache = TTLCache(maxsize=1000, ttl=10)


@app.get("/")
async def index():
    return {"Hello": "World"}


@cached(cache)
@app.get("/stock/{ticker}")
async def get_stock(ticker: str):
    return get_stock_data(ticker)
