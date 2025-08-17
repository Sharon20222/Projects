import pandas as pd
import numpy as np

def total_return(equity: pd.Series) -> float:
    """Calculate total return."""
    return equity.iloc[-1] / equity.iloc[0] - 1

def cagr(equity: pd.Series, periods_per_year: int = 252) -> float:
    """Compound Annual Growth Rate (CAGR)."""
    n_years = len(equity) / periods_per_year
    return (equity.iloc[-1] / equity.iloc[0]) ** (1 / n_years) - 1

def sharpe_ratio(equity: pd.Series, risk_free_rate: float = 0, periods_per_year: int = 252) -> float:
    """Annualized Sharpe Ratio."""
    returns = equity.pct_change().dropna()
    excess_returns = returns - (risk_free_rate / periods_per_year)
    return np.sqrt(periods_per_year) * excess_returns.mean() / excess_returns.std()

def max_drawdown(equity: pd.Series) -> float:
    """Maximum drawdown."""
    cum_max = equity.cummax()
    drawdown = (equity - cum_max) / cum_max
    return drawdown.min()
