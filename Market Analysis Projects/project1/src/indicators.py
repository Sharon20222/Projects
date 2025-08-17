import pandas as pd
import numpy as np

def sma(series: pd.Series, window: int) -> pd.Series:
    """Simple Moving Average"""
    return series.rolling(window=window).mean()

def ema(series: pd.Series, window: int) -> pd.Series:
    """Exponential Moving Average"""
    return series.ewm(span=window, adjust=False).mean()

def rsi(series: pd.Series, window: int = 14) -> pd.Series:
    """Relative Strength Index (RSI)"""
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    """MACD (returns MACD line and Signal line)"""
    fast_ema = ema(series, fast)
    slow_ema = ema(series, slow)
    macd_line = fast_ema - slow_ema
    signal_line = ema(macd_line, signal)
    return macd_line, signal_line

def bollinger_bands(series: pd.Series, window: int = 20, num_std: int = 2):
    """Bollinger Bands (returns upper, lower bands)"""
    sma_ = sma(series, window)
    rolling_std = series.rolling(window).std()
    upper = sma_ + num_std * rolling_std
    lower = sma_ - num_std * rolling_std
    return upper, lower
