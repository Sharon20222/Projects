import numpy as np
import pandas as pd

def correlation_matrix(df, method="pearson"):
    """
    Compute correlation matrix for a DataFrame of returns.

    Parameters:
        df (pd.DataFrame): Daily returns DataFrame.
        method (str): 'pearson' or 'spearman'

    Returns:
        pd.DataFrame: Correlation matrix
    """
    return df.corr(method=method)

def portfolio_metrics(returns, weights=None):
    """
    Calculate portfolio metrics: return, volatility, Sharpe ratio.

    Parameters:
        returns (pd.DataFrame): Daily returns of assets.
        weights (list or np.array): Portfolio weights. Equal weighting if None.

    Returns:
        dict: Portfolio metrics
    """
    if weights is None:
        weights = np.array([1/returns.shape[1]]*returns.shape[1])
    else:
        weights = np.array(weights)
    
    portfolio_return = np.dot(returns.mean()*252, weights)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov()*252, weights)))
    sharpe_ratio = portfolio_return / portfolio_volatility

    return {
        "Expected Annual Return": portfolio_return,
        "Annual Volatility": portfolio_volatility,
        "Sharpe Ratio": sharpe_ratio
    }

def monte_carlo_var(returns, weights=None, confidence_level=0.05, simulations=10000):
    """
    Estimate portfolio Value at Risk (VaR) using Monte Carlo simulation.

    Parameters:
        returns (pd.DataFrame): Daily returns.
        weights (list or np.array): Portfolio weights.
        confidence_level (float): e.g., 0.05 for 95% confidence.
        simulations (int): Number of simulated portfolio returns.

    Returns:
        float: Value at Risk
    """
    if weights is None:
        weights = np.array([1/returns.shape[1]]*returns.shape[1])
    else:
        weights = np.array(weights)
    
    mean = returns.mean()
    cov = returns.cov()
    
    simulated_returns = np.random.multivariate_normal(mean, cov, simulations)
    portfolio_returns = simulated_returns.dot(weights)
    var = np.percentile(portfolio_returns, 100*confidence_level)
    
    return var
