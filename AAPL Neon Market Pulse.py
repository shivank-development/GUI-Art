import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")

# Download stock data
p = yf.download("AAPL", period="3mo", progress=False)["Close"]

# Calculate returns
r = p.pct_change().fillna(0).values
x = np.arange(len(p))

# Plot
plt.figure(figsize=(10, 4))

sc = plt.scatter(x, p, c=r, cmap="plasma", s=45)
plt.plot(x, p, c="#ff00ff", lw=1, alpha=0.6)

plt.title("AAPL Neon Market Pulse", weight="bold")
plt.axis("off")
plt.colorbar(sc, label="Return Intensity")

plt.tight_layout()
plt.show()
