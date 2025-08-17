
```markdown
# Commodities Technical Analysis & Backtesting

This project is a **Python-based framework** for analyzing commodities markets, testing trading strategies, and evaluating performance.  
It is designed to be **clear, extensible, and portfolio-ready** — something you can proudly showcase on GitHub.

---

## ✨ Features
- 📈 **Data Collection**: Download historical prices from Yahoo Finance (`yfinance`)
- ⚡ **Technical Indicators**: SMA, EMA, RSI, MACD, Bollinger Bands
- 🧠 **Strategies Implemented**:
  - Simple Moving Average (SMA) Crossover
  - RSI Mean Reversion
- 🔄 **Backtesting Engine**:
  - Vectorized calculations (fast + clean)
  - Transaction costs and slippage support
- 📊 **Performance Metrics**:
  - Total Return
  - CAGR
  - Sharpe Ratio
  - Maximum Drawdown
- 📑 **Reports**:
  - Markdown report automatically generated
  - Equity curve charts saved as PNG



## ⚙️ Installation
```bash
# Clone the repo
git clone https://github.com/<your-username>/commodities-ta-backtest.git
cd commodities-ta-backtest

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
````

---

## 🚀 Usage

### Run SMA Crossover Strategy

Example: crude oil futures (`CL=F`)

```bash
python src/main.py --ticker CL=F --start 2015-01-01 \
  --strategy sma_cross --fast 20 --slow 50 --fee_bps 1 --slippage_bps 1
```

### Run RSI Mean Reversion Strategy

Example: natural gas futures (`NG=F`)

```bash
python src/main.py --ticker NG=F --start 2015-01-01 \
  --strategy rsi_reversion --rsi_window 14 --rsi_lower 30 --rsi_upper 70
```

---

## 📊 Example Output

* `reports/CL=F_sma_cross_report.md`
* `reports/CL=F_sma_cross_equity.png`

The report contains:

* Performance metrics
* Equity curve chart

---

## 🔮 Future Extensions

* Portfolio backtesting (multi-asset)
* Risk parity allocation
* More advanced strategies (MACD, Bollinger Bands, ML-driven)
* Interactive dashboards with Streamlit/Plotly

---

## 🛠️ Requirements

* Python 3.8+
* See `requirements.txt` for dependencies

---

## 📜 License

MIT License – free to use, modify, and distribute.

```

---
