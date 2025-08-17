
````markdown
# Trading Strategy Backtester

A Python project for analyzing and backtesting trading strategies on historical market data.  
This project combines **data analysis** with **quantitative trading** concepts, allowing you to test strategies like SMA crossovers and RSI mean-reversion on assets such as commodities, stocks, or indices.

---

## Features

- Download historical market data from Yahoo Finance using `yfinance`.
- Calculate technical indicators: SMA, EMA, RSI, MACD, Bollinger Bands.
- Define and apply strategies:
  - SMA Crossover
  - RSI Mean Reversion
- Backtest strategies with fees and slippage.
- Compute performance metrics: Total Return, CAGR, Sharpe Ratio, Max Drawdown.
- Visualize equity curves.
- Generate a simple strategy report.

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/trading-backtester.git
cd trading-backtester
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

* The default example downloads **Crude Oil Futures (CL=F)** data.
* You can switch strategies by commenting/uncommenting in `main.py`:

```python
strategy_df = sma_crossover_strategy(df, fast=20, slow=50)
# strategy_df = rsi_mean_reversion_strategy(df, window=14, lower=30, upper=70)
```

* Backtesting includes optional transaction fees (`fee_bps`) and slippage (`slippage_bps`).

* Reports are printed in the console and equity curves saved as PNG.

---

## Example Output

**Equity Curve:**

![Equity Curve](CL=F_equity.png)

**Metrics Output:**

```
=== CL=F Strategy Report ===
Total Return: 0.3524
CAGR: 0.1123
Sharpe Ratio: 1.15
Max Drawdown: -0.18
```

---

## Project Structure

```
project_root/
│
├─ README.md
├─ requirements.txt
├─ main.py
└─ src/
   ├─ data.py          # Download market data
   ├─ indicators.py    # Technical indicators
   ├─ strategies.py    # Trading strategies
   ├─ backtest.py      # Backtesting engine
   ├─ metrics.py       # Performance metrics
   ├─ plot.py          # Plotting equity curves
   └─ report.py        # Strategy report
```

---

## Dependencies

* Python >= 3.8
* pandas
* numpy
* yfinance
* matplotlib

Install with:

```bash
pip install -r requirements.txt
```

---

## Contributing

Feel free to fork the repo and add:

* New strategies
* Additional technical indicators
* Portfolio backtesting
* Visualization improvements

---

