import matplotlib.pyplot as plt

def plot_equity_curve(df, title: str = "Equity Curve", filename: str = None):
    """
    Plot the equity curve.
    
    Parameters
    ----------
    df : pd.DataFrame
        Must contain 'Equity' column.
    title : str
        Chart title.
    filename : str
        If provided, save the figure as PNG.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['Equity'], label='Equity Curve', color='blue')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Equity")
    plt.grid(True)
    plt.legend()
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()
