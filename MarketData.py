import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def get_stock_data():
    print("STOCK DATA FETCHER")
    print("=" * 40)

    ticker = input("Enter ticker symbol (e.g. AAPL): ").upper()
    timeframe = input("Enter timeframe (1d, 5d, 1mo, 6mo, 1y): ")

    print("\n🔄 Fetching data...\n")

    stock = yf.Ticker(ticker)
    df = stock.history(period=timeframe)

    if df.empty:
        print("No data found. Check the ticker or timeframe.")
        return


    try:
        company_name = stock.info.get("longName", ticker)
    except:
        company_name = ticker

    latest_close = round(df["Close"].iloc[-1], 2)

    print(f"Company: {company_name}")
    print(f" Latest Close: ${latest_close}")
    print(f" Records Returned: {len(df)}\n")

    display_df = df[["Open", "High", "Low", "Close", "Volume"]].copy()
    display_df = display_df.round(2)

    print(display_df.to_string())

    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["Close"], marker="o")
    plt.title(f"{ticker} Closing Price ({timeframe})")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    get_stock_data()
