import yfinance as yf
import matplotlib.pyplot as plt

ticker = input("Enter Stock Name (Example: AAPL, TSLA, RELIANCE.NS): ")

# Fetch data
data = yf.download(
    ticker,
    start="2021-01-01",
    end="2025-11-13",
    auto_adjust=False
)

# Check if data is empty
if data.empty:
    print("❌ Invalid stock symbol or no data found!")
else:
    plt.figure(figsize=(12, 6))
    plt.plot(data["Close"], label="Closing Price", linewidth=2)

    plt.title(f"{ticker.upper()} Stock Price Chart (2021–2025)", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Stock Price", fontsize=12)

    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
