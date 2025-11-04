import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------------------------------
# TASK 2(a) - Categorical Univariate Analysis
# ------------------------------------------

df_cat = pd.read_csv("customer_purchase.csv")
print(df_cat.head())

print(df_cat['Product_Category'].value_counts())
print(df_cat['Payment_Mode'].value_counts())

# Bar Chart for Product Category
plt.figure(figsize=(6,4))
sns.countplot(x='Product_Category', data=df_cat)
plt.title("Product Category Distribution")
plt.show()

# Pie Chart for Payment Mode
df_cat['Payment_Mode'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Payment Mode Distribution")
plt.show()

# Optional
sns.countplot(x='Gender', data=df_cat)
plt.title("Customers by Gender")
plt.show()

# ------------------------------------------
# TASK 2(b) - Continuous Univariate Analysis
# ------------------------------------------

df_cont = pd.read_csv("sensor_readings.csv")
print(df_cont.head())

# Histogram (Temperature)
sns.histplot(df_cont['Temperature_C'])
plt.show()

# KDE Density (Humidity)
sns.kdeplot(df_cont['Humidity_%'], shade=True)
plt.show()

# Rug Plot (Temperature)
sns.rugplot(df_cont['Temperature_C'])
plt.show()

# Strip Plot (Air Quality)
sns.stripplot(x=df_cont['Air_Quality_Index'])
plt.show()

# Line Plot (Time vs Temperature)
sns.lineplot(x='Time', y='Temperature_C', data=df_cont)
plt.show()

# Scatterplot (Temp vs Humidity)
sns.scatterplot(x='Temperature_C', y='Humidity_%', data=df_cont)
plt.show()

# Summary Statistics
print(df_cont.describe())
print("Skewness:", df_cont['Air_Quality_Index'].skew())
print("Kurtosis:", df_cont['Air_Quality_Index'].kurt())
