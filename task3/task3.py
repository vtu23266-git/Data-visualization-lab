import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

# ------------------ TASK 3(a) ------------------
df1 = pd.read_csv("hr1.csv")
print(df1.head())

# Stacked Bar - Gender vs Promotion Status
pd.crosstab(df1['Gender'], df1['Promotion_Status']).plot(kind='bar', stacked=True)
plt.show()

# Grouped Bar - Gender vs Promotion Status
pd.crosstab(df1['Gender'], df1['Promotion_Status']).plot(kind='bar')
plt.show()

# Segmented Bar - Department vs Job Level
pd.crosstab(df1['Department'], df1['Job_Level']).plot(kind='bar', stacked=True)
plt.show()

# Mosaic Plot - Education vs Promotion
mosaic(df1, ['Education_Level', 'Promotion_Status'])
plt.show()


# ------------------ TASK 3(b) ------------------
df2 = pd.read_csv("hr2.csv")
print(df2.describe())

# Scatter + Regression
sns.regplot(x='Age', y='Salary', data=df2)
plt.show()

# Scatter with Hue by Experience Quartile
df2['Group'] = pd.qcut(df2['Experience_Years'], 4)
sns.scatterplot(x='Experience_Years', y='Satisfaction_Score', hue='Group', data=df2)
plt.show()

# Correlation Heatmap
sns.heatmap(df2.corr(), annot=True)
plt.show()


# ------------------ TASK 3(c) ------------------
df3 = pd.read_csv("hr3.csv")

# Bar - Avg Salary per Department
df3.groupby('Department')['Salary'].mean().plot(kind='bar')
plt.show()

# Box - Satisfaction by Gender
sns.boxplot(x='Gender', y='Satisfaction_Score', data=df3)
plt.show()

# Violin - Working Hours by Department
sns.violinplot(x='Department', y='Working_Hours', data=df3)
plt.show()

# Beeswarm Plot
sns.swarmplot(x='Gender', y='Satisfaction_Score', data=df3)
plt.show()

# KDE Grouped by Gender
for g in df3['Gender'].unique():
    sns.kdeplot(df3[df3['Gender']==g]['Age'], shade=True, label=g)
plt.legend()
plt.show()
