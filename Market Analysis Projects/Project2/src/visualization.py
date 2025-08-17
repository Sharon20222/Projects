import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_correlation_heatmap(corr_matrix, filename="correlation_heatmap.png"):
    """
    Plot and save correlation heatmap.

    Parameters:
        corr_matrix (pd.DataFrame): Correlation matrix
        filename (str): File name to save the plot
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def plot_portfolio_equity_curve(returns, weights=None, filename="portfolio_equity_curve.png"):
    """
    Plot cumulative equity curve for portfolio.

    Parameters:
        returns (pd.DataFrame): Daily returns
        weights (list or np.array): Portfolio weights. Equal if None
        filename (str): File name to save the plot
    """
    if weights is None:
        weights = np.array([1/returns.shape[1]]*returns.shape[1])
    else:
        weights = np.array(weights)
    
    portfolio_daily_returns = returns.dot(weights)
    cumulative_returns = (1 + portfolio_daily_returns).cumprod()
    
    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_returns, label="Portfolio Equity")
    plt.title("Portfolio Equity Curve")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Returns")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def plot_risk_return(returns, weights=None, filename="risk_return_scatter.png"):
    """
    Plot risk/return scatter for individual assets.

    Parameters:
        returns (pd.DataFrame): Daily returns
        weights (list or np.array): Portfolio weights (optional)
        filename (str): File name to save the plot
    """
    annual_returns = returns.mean()*252
    annual_volatility = returns.std()*np.sqrt(252)

    plt.figure(figsize=(10, 6))
    plt.scatter(annual_volatility, annual_returns, marker='o')
    
    for i, ticker in enumerate(returns.columns):
        plt.annotate(ticker, (annual_volatility[i], annual_returns[i]))
    
    if weights is not None:
        portfolio_return = np.dot(annual_returns, weights)
        portfolio_vol = np.sqrt(np.dot(weights.T, np.dot(returns.cov()*252, weights)))
        plt.scatter(portfolio_vol, portfolio_return, color='red', marker='*', s=200, label='Portfolio')
        plt.legend()

    plt.xlabel("Annual Volatility")
    plt.ylabel("Annual Return")
    plt.title("Risk vs Return")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
