import yfinance as yf
import pandas as pd

def get_stock_data():
    print("welcome to my stock data fetcher!")
    print("---------------------------------")
    
    t = input("enter a ticker symbol (like AAPL): ")
    tf = input("enter timeframe (1d, 5d, 1mo, 1y): ")
    
    print("\nfetching data...\n")
    
    stock = yf.Ticker(t)
    df = stock.history(period=tf)
    
    if df.empty:
        print("no data found. maybe a bad ticker or timeframe?")
        return
        
    print("Date       | Open   | High   | Low    | Close  | Volume")
    print("-" * 65)
    
    for index, row in df.iterrows():
        d = str(index).split(" ")[0]
        o = round(row['Open'], 2)
        h = round(row['High'], 2)
        l = round(row['Low'], 2)
        c = round(row['Close'], 2)
        v = int(row['Volume'])
        
        print(f"{d} | {o}\t| {h}\t| {l}\t| {c}\t| {v}")

if __name__ == "__main__":
    get_stock_data()