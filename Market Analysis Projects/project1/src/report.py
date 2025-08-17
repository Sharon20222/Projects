from .metrics import total_return, cagr, sharpe_ratio, max_drawdown
from .plot import plot_equity_curve

def generate_report(df, title="Strategy Report", plot_filename=None):
    """
    Generate a simple report of strategy performance.
    
    Parameters
    ----------
    df : pd.DataFrame
        Must contain 'Equity' column.
    title : str
        Report title.
    plot_filename : str
        Filename to save the equity curve plot.
    """
    # Compute metrics
    metrics_dict = {
        "Total Return": total_return(df['Equity']),
        "CAGR": cagr(df['Equity']),
        "Sharpe Ratio": sharpe_ratio(df['Equity']),
        "Max Drawdown": max_drawdown(df['Equity'])
    }

    # Print metrics
    print(f"=== {title} ===")
    for k, v in metrics_dict.items():
        print(f"{k}: {v:.4f}")
    
    # Plot equity curve
    plot_equity_curve(df, title=title, filename=plot_filename)
