import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates, scatter_matrix

df = pd.read_csv("employee_multivariate.csv")
print(df.head())

# 1. Scatterplot Matrix
sns.pairplot(df, vars=['Age','Years_of_Experience','Monthly_Salary','Satisfaction_Score'], hue='Department')
plt.show()

# 2. Parallel Coordinates
parallel_coordinates(df[['Department','Job_Level','Age','Monthly_Salary','Working_Hours_per_Week']], 'Department')
plt.show()

# 3. Line Graph - Salary vs Experience per Department
sns.lineplot(x='Years_of_Experience', y='Monthly_Salary', hue='Department', data=df)
plt.show()

# 4. Stacked Bar - Dept vs Job Level
pd.crosstab(df['Department'], df['Job_Level']).plot(kind='bar', stacked=True)
plt.show()
