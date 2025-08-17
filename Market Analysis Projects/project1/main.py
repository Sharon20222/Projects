from src.data import download_data
from src.strategies import sma_crossover_strategy, rsi_mean_reversion_strategy
from src.backtest import backtest
from src.report import generate_report

def main():
    # 1. Download data (example: Crude Oil Futures)
    ticker = "CL=F"
    df = download_data(ticker, start="2018-01-01")
    
    # 2. Apply strategy (choose one)
    strategy_df = sma_crossover_strategy(df, fast=20, slow=50)
    # strategy_df = rsi_mean_reversion_strategy(df, window=14, lower=30, upper=70)
    
    # 3. Backtest
    backtested_df = backtest(strategy_df, fee_bps=5, slippage_bps=2)
    
    # 4. Generate report
    generate_report(backtested_df, title=f"{ticker} Strategy Report", plot_filename=f"{ticker}_equity.png")

if __name__ == "__main__":
    main()
