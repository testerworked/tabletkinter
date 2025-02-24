import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

# Generate mock data for Ethereum prices for demonstration
np.random.seed(42)  # For reproducibility
data_size = 1000
categories = ['Low', 'Medium', 'High']  # Mock 'cut' categories

# Create a DataFrame with random Ethereum price data
ethereum_price_data = {
    'price': np.random.lognormal(mean=3, sigma=1, size=data_size),  # Log-normal distribution
    'category': np.random.choice(categories, size=data_size)
}

df_ethereum = pd.DataFrame(ethereum_price_data)

# Plotting
sns.set_theme(style="ticks")

f, ax = plt.subplots(figsize=(10, 6))
sns.despine(f)

sns.histplot(
    df_ethereum,
    x="price", hue="category",
    multiple="stack",
    palette="light:m_r",
    edgecolor=".3",
    linewidth=.5,
    log_scale=True,
)

# Setting the x-axis with a greater range
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
ax.set_xticks([50, 100, 200, 500, 1000, 2000, 5000, 10000])

# Labels and title
ax.set_xlabel('Ethereum Price in USDT')
ax.set_ylabel('Count')
ax.set_title('Distribution of Ethereum Prices in USDT by Category')

plt.show()