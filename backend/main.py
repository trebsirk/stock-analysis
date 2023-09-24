from typing import Union

from fastapi import FastAPI
from stocks import get_stock_data

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/stock/{ticker}")
async def read_item(ticker: str):
    return get_stock_data(ticker)
