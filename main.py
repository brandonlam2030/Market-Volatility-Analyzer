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


mean = returns.mean()

stability = abs(returns-mean)

num_unstable = len(stability[stability["SPY"] > .01])
print(num_unstable/len(stability["SPY"])*100)



plt.subplot(1,2,2)
plt.plot(returns)
plt.title("Returns Per Day")
plt.show()