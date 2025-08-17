
````markdown
# Multi-Asset Correlation & Portfolio Risk Dashboard

A Python project for analyzing correlations among multiple financial assets and evaluating portfolio risk metrics.  
This project demonstrates **market analysis, portfolio risk modeling, and visualization** skills.

---

## Features

- Download historical market data from Yahoo Finance using `yfinance`.
- Compute daily returns for multiple assets.
- Calculate correlation matrices (Pearson and Spearman).
- Portfolio risk metrics:
  - Portfolio returns
  - Portfolio volatility
  - Sharpe ratio
  - Monte Carlo simulation for Value at Risk (VaR)
- Visualizations:
  - Correlation heatmap
  - Portfolio equity curve
  - Risk/Return scatter plot
- Optional interactive dashboard using `streamlit`.

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/multi-asset-risk.git
cd multi-asset-risk
````

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main script:

```bash
python main.py
```

* Example tickers: `AAPL, MSFT, SPY, GLD, BTC-USD`
* Outputs:

  * `correlation_heatmap.png`
  * `portfolio_equity_curve.png`
  * Portfolio metrics printed to console

---

## Example Output

**Correlation Heatmap:**

![Correlation Heatmap](correlation_heatmap.png)

**Portfolio Metrics:**

```
=== Portfolio Report ===
Expected Annual Return: 12.5%
Annual Volatility: 18.3%
Sharpe Ratio: 0.68
95% Value at Risk: -7.2%
```

---

## Project Structure

```
market_analysis_project/
│
├─ README.md
├─ requirements.txt
├─ main.py
└─ src/
   ├─ data.py          # Download and clean market data
   ├─ analysis.py      # Correlation and portfolio metrics
   ├─ visualization.py # Heatmaps, equity curves, risk plots
   └─ dashboard.py     # Optional Streamlit dashboard
```

---

## Dependencies

* Python >= 3.8
* pandas
* numpy
* matplotlib
* seaborn
* yfinance
* streamlit (optional)

Install with:

```bash
pip install -r requirements.txt
```



