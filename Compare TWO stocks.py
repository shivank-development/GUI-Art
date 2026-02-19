import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stocks = ["AAPL", "MSFT"]

plt.figure(figsize=(10, 4))

for s in stocks:
    d = yf.download(s, period="3mo", progress=False)["Close"]
    plt.plot(d.pct_change(), label=s)

plt.title("Return Comparison (Behavior View)")
plt.legend()
plt.tight_layout()
plt.show()
