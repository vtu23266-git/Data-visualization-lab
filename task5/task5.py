import pandas as pd
import plotly.express as px
import squarify

# --------- 5(a) TreeMap ---------
df_tree = pd.read_csv("products_sales.csv")
fig = px.treemap(df_tree, path=['Category','Subcategory','Product'], values='Sales_Amount', color='Category')
fig.show()

# --------- 5(b) Sunburst ---------
df_sun = pd.read_csv("company_structure.csv")
fig2 = px.sunburst(df_sun, path=['Company','Division','Team','Employee_Name'], values='Salary', color='Division')
fig2.show()
