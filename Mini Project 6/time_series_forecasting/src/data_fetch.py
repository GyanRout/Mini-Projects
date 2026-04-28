import yfinance as yf
import pandas as pd
import config

def download_data():
    stock = yf.Ticker(config.TICKER)
    df = stock.history(start=config.START_DATE, end=config.END_DATE)
    df = df[['Close']]
    print("Saving the DataFrame")
    df.to_csv(config.DATA_PATH)

if __name__ == "__main__":
    download_data()