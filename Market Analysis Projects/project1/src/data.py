import yfinance as yf
import pandas as pd

def download_data(ticker: str, start: str = "2015-01-01", end: str = None) -> pd.DataFrame:
    """
    Download historical price data from Yahoo Finance.
    
    Parameters
    ----------
    ticker : str
        Yahoo Finance ticker symbol (e.g., "CL=F" for crude oil).
    start : str
        Start date for data (YYYY-MM-DD).
    end : str
        End date for data (YYYY-MM-DD). If None, uses today.
    
    Returns
    -------
    pd.DataFrame
        Historical OHLCV price data.
    """
    df = yf.download(ticker, start=start, end=end, progress=False)
    df = df[["Open", "High", "Low", "Close", "Adj Close", "Volume"]]
    df.dropna(inplace=True)
    return df
