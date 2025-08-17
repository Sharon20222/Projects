import yfinance as yf
import pandas as pd

def download_data(tickers, start="2018-01-01", end=None):
    """
    Download historical adjusted close prices for a list of tickers.

    Parameters:
        tickers (list): List of ticker symbols (e.g., ['AAPL', 'MSFT']).
        start (str): Start date in 'YYYY-MM-DD' format.
        end (str): End date in 'YYYY-MM-DD' format. Default None = today.

    Returns:
        pd.DataFrame: Adjusted close prices, tickers as columns.
    """
    data = yf.download(tickers, start=start, end=end)['Adj Close']
    data = data.dropna()
    return data

def calculate_daily_returns(df):
    """
    Compute daily returns from price data.

    Parameters:
        df (pd.DataFrame): DataFrame of adjusted close prices.

    Returns:
        pd.DataFrame: Daily returns.
    """
    returns = df.pct_change().dropna()
    return returns
