from typing import Union

from fastapi import FastAPI
from stocks.stocks import get_stock_data

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/stock/{ticker}")
async def get_stock(ticker: str):
    raw: dict = get_stock_data(ticker)
    return raw
