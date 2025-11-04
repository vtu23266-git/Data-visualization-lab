import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df_net = pd.read_csv("network_edges.csv")

G = nx.from_pandas_edgelist(df_net, 'Source', 'Target')

pos = nx.spring_layout(G)   # Force-directed layout
nx.draw(G, pos, with_labels=True, node_size=600, font_weight='bold')
plt.show()

# Centrality Example
print("Degree Centrality:", nx.degree_centrality(G))
