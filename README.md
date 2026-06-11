# Stock Data Fetcher

https://github.com/user-attachments/assets/ffeea231-8449-4761-bb97-3e13a7005878


hey! this is a small python script i made to pull stock data from yahoo finance. it asks for a ticker and a timeframe and then prints out a table with all the data (ohlcv). 

i used the `yfinance` library to get the data easily.

## How to Run it

### 1. install libraries
you need to install `yfinance` and `pandas` first or it won't work. run this in your terminal:

```bash
pip install yfinance pandas
```

### 2. Run the Script
just run it with python:

```bash
python MarketData.py
```

## How to Use it
when you run the script, it will ask you for two things:
1. **ticker symbol:** enter something like `AAPL`, `TSLA`, or `MSFT` (make sure it's uppercase just in case).
2. **timeframe:** enter how much data you want to see. valid options are `1d`, `5d`, `1mo`, or `1y`.

## Things I Want to Fix Later
* make the table columns line up perfectly because right now tabs (`\t`) make it look a little weird if the numbers are too big.
* let the user pass the ticker directly in the terminal command instead of typing it after it starts.
