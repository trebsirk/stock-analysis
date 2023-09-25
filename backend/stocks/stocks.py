import yfinance as yf


def get_stock_data(ticker: str):
    print(f'getting {ticker} data')
    try:
        price_history = yf.Ticker(ticker).history(
            period="5d",  # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            interval="1d",  # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            actions=False,
        )
        print(f'got {ticker} data')
        return price_history.to_dict()
    except Exception as e:
        print(f'error getting {ticker} data: {e}')
        return {}


def transform_stock_data(data: dict):
    return data