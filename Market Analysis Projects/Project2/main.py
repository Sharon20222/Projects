from src.data import download_data, calculate_daily_returns
from src.analysis import correlation_matrix, portfolio_metrics, monte_carlo_var
from src.visualization import plot_correlation_heatmap, plot_portfolio_equity_curve, plot_risk_return

def main():
    # Step 1: Define tickers
    tickers = ["AAPL", "MSFT", "SPY", "GLD", "BTC-USD"]

    # Step 2: Download historical data
    data = download_data(tickers, start="2018-01-01")
    
    # Step 3: Calculate daily returns
    returns = calculate_daily_returns(data)
    
    # Step 4: Correlation analysis
    corr = correlation_matrix(returns)
    print("=== Correlation Matrix ===")
    print(corr)
    
    # Step 5: Portfolio metrics (equal weight)
    weights = None  # Equal weights
    metrics = portfolio_metrics(returns, weights)
    var_95 = monte_carlo_var(returns, weights, confidence_level=0.05)
    
    print("\n=== Portfolio Report ===")
    for k, v in metrics.items():
        print(f"{k}: {v:.2%}")
    print(f"95% Value at Risk (VaR): {var_95:.2%}")
    
    # Step 6: Visualizations
    plot_correlation_heatmap(corr)
    plot_portfolio_equity_curve(returns, weights)
    plot_risk_return(returns, weights)
    
    print("\nPlots saved: correlation_heatmap.png, portfolio_equity_curve.png, risk_return_scatter.png")

if __name__ == "__main__":
    main()
