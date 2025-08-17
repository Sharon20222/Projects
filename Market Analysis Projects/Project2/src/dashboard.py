import streamlit as st
from src.data import download_data, calculate_daily_returns
from src.analysis import correlation_matrix, portfolio_metrics, monte_carlo_var
from src.visualization import plot_correlation_heatmap, plot_portfolio_equity_curve, plot_risk_return
import pandas as pd

st.title("Multi-Asset Correlation & Portfolio Risk Dashboard")

# Step 1: User input
tickers_input = st.text_input("Enter tickers separated by commas (e.g., AAPL,MSFT,SPY,GLD,BTC-USD):", "AAPL,MSFT,SPY,GLD,BTC-USD")
tickers = [t.strip() for t in tickers_input.split(",")]

start_date = st.date_input("Start Date", pd.to_datetime("2018-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("today"))

# Step 2: Download data
data = download_data(tickers, start=start_date, end=end_date)

st.subheader("Historical Prices")
st.line_chart(data)

# Step 3: Daily returns
returns = calculate_daily_returns(data)

# Step 4: Correlation heatmap
st.subheader("Correlation Heatmap")
corr = correlation_matrix(returns)
st.dataframe(corr)
plot_correlation_heatmap(corr, "dashboard_correlation.png")
st.image("dashboard_correlation.png")

# Step 5: Portfolio metrics
st.subheader("Portfolio Metrics")
weights_input = st.text_input("Enter weights separated by commas (leave blank for equal weights):")
if weights_input:
    weights = [float(w.strip()) for w in weights_input.split(",")]
else:
    weights = None

metrics = portfolio_metrics(returns, weights)
var_95 = monte_carlo_var(returns, weights)

for k, v in metrics.items():
    st.write(f"{k}: {v:.2%}")
st.write(f"95% Value at Risk (VaR): {var_95:.2%}")

# Step 6: Visualizations
st.subheader("Portfolio Equity Curve")
plot_portfolio_equity_curve(returns, weights, "dashboard_equity.png")
st.image("dashboard_equity.png")

st.subheader("Risk vs Return Scatter")
plot_risk_return(returns, weights, "dashboard_risk_return.png")
st.image("dashboard_risk_return.png")
