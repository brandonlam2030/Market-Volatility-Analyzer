import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


tickers = ["SPY", "BND", "GLD", "VTI", "QQQ"]
end_date = datetime.today()
start_date = end_date - timedelta(days = 365)
close_df = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker,start = start_date, end = end_date)
    close_df[ticker] = data["Close"]

close_df.dropna(inplace = True)

returns = np.log(close_df/close_df.shift(1))
returns.dropna(inplace = True)


rolling_vol = returns.rolling(21).std()
rolling_vol.dropna(inplace=True)

rolling_mean = rolling_vol.mean()
unstable = rolling_vol.gt(rolling_mean, axis = 1)

unstable_ratio = unstable.mean()
print("Instability Ratios\n" + (unstable_ratio*100).to_string())





plt.plot(rolling_vol, lw = 3)
plt.legend(tickers)
plt.title("Rolling Volatility Over the Year")
plt.show()