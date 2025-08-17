import pandas as pd

def backtest(df: pd.DataFrame, fee_bps: float = 0, slippage_bps: float = 0) -> pd.DataFrame:
    """
    Backtest a trading strategy given price data and signals.
    
    Parameters
    ----------
    df : pd.DataFrame
        Must contain 'Close' and 'Position' columns.
    fee_bps : float
        Transaction fee in basis points (1 bp = 0.01%).
    slippage_bps : float
        Slippage in basis points.
    
    Returns
    -------
    pd.DataFrame
        df with equity curve and returns.
    """
    df = df.copy()
    
    # Calculate returns
    df['Return'] = df['Close'].pct_change()
    
    # Shift positions to apply returns on next day
    df['Strategy_Return'] = df['Return'] * df['Position'].shift(1)
    
    # Apply fees and slippage on trade days
    trade_days = df['Position'].diff().fillna(0) != 0
    total_cost = (fee_bps + slippage_bps) / 10000
    df.loc[trade_days, 'Strategy_Return'] -= total_cost
    
    # Calculate equity curve
    df['Equity'] = (1 + df['Strategy_Return']).cumprod()
    
    return df
