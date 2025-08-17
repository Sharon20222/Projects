import pandas as pd
from .indicators import sma, rsi

def sma_crossover_strategy(df: pd.DataFrame, fast: int = 20, slow: int = 50) -> pd.DataFrame:
    """
    Simple Moving Average Crossover Strategy.
    
    Buy when fast SMA crosses above slow SMA.
    Sell when fast SMA crosses below slow SMA.
    """
    df = df.copy()
    df['SMA_fast'] = sma(df['Close'], fast)
    df['SMA_slow'] = sma(df['Close'], slow)
    
    df['Signal'] = 0
    df['Signal'][fast:] = \
        (df['SMA_fast'][fast:] > df['SMA_slow'][fast:]).astype(int)
    
    df['Position'] = df['Signal'].diff()
    return df

def rsi_mean_reversion_strategy(df: pd.DataFrame, window: int = 14, lower: int = 30, upper: int = 70) -> pd.DataFrame:
    """
    RSI Mean Reversion Strategy.
    
    Buy when RSI < lower threshold.
    Sell when RSI > upper threshold.
    """
    df = df.copy()
    df['RSI'] = rsi(df['Close'], window)
    
    df['Signal'] = 0
    df['Signal'][df['RSI'] < lower] = 1   # Buy
    df['Signal'][df['RSI'] > upper] = -1  # Sell
    
    df['Position'] = df['Signal'].replace(to_replace=0, method='ffill')
    return df
