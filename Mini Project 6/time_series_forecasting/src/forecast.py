import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import config
from statsmodels.tsa.arima.model import ARIMA

def run_forecast():
    df = pd.read_csv(config.DATA_PATH, index_col=0)
    df.index = pd.to_datetime(df.index, utc=True).tz_localize(None)
    series = df['Close']

    model = ARIMA(series, order=(5, 1, 0))
    fitted_model = model.fit()
    predictions = fitted_model.forecast(steps=config.FORECAST_STEPS)
    
    last_date = series.index[-1]
    future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=config.FORECAST_STEPS, freq='B')
    predictions.index = future_dates

    # Visualization
    plt.figure(figsize=(12, 6))
    plt.plot(series[-100:], label='Historical')
    plt.plot(predictions, color='red', label='Forecast')
    plt.title(f"{config.TICKER} Price Forecast")
    plt.legend()
    
    plt.savefig("forecast_output.png")
    print("Success! Forecast saved to forecast_output.png")

if __name__ == "__main__":
    run_forecast()