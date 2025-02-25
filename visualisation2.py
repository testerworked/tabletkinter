import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme(style="ticks", palette="pastel")

crypto_data = pd.read_csv('crypto_data.csv')

sns.scatterplot(x="BTC", y="ETH", data=crypto_data)

sns.despine(offset=10, trim=True)
plt.title('Зависимость Ethereum от Bitcoin')
plt.xlabel('Bitcoin Price (BTC)')
plt.ylabel('Ethereum Price (ETH)')
plt.show()