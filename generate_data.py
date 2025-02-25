import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2023-01-31", freq="D")  # 31 days
btc_prices = np.random.normal(loc=30000, scale=1000, size=len(dates)).round(2)  # BTC prices around $30,000
eth_prices = np.random.normal(loc=2000, scale=100, size=len(dates)).round(2)  # ETH prices around $2,000

crypto_data = pd.DataFrame({
    "Date": dates,
    "BTC": btc_prices,
    "ETH": eth_prices
})

# Save to CSV
crypto_data.to_csv("crypto_data.csv", index=False)

print("Sample crypto_data.csv file generated!")