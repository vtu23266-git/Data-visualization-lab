import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df_sales = pd.read_csv("sales_data.csv", parse_dates=['Date'])
df_sales.set_index('Date', inplace=True)

# Trend Line
df_sales['Sales'].plot(); plt.title("Sales Trend"); plt.show()

# Profit
df_sales['Profit'].plot(); plt.title("Profit Trend"); plt.show()

# Margin
df_sales['Margin'] = df_sales['Profit'] / df_sales['Sales']
df_sales['Margin'].plot(); plt.title("Margin Trend"); plt.show()

# Box Plot by Month
df_sales['Month'] = df_sales.index.month
sns.boxplot(x='Month', y='Sales', data=df_sales)
plt.show()

# Heatmap
df_sales['Year'] = df_sales.index.year
pivot = df_sales.pivot_table(values='Sales', index='Year', columns='Month')
sns.heatmap(pivot, annot=True); plt.show()

# Lag & Autocorrelation
from pandas.plotting import lag_plot, autocorrelation_plot
lag_plot(df_sales['Sales']); plt.show()
autocorrelation_plot(df_sales['Sales']); plt.show()
