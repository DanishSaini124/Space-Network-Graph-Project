import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+top+100+hostname,pl_name+from+ps&format=csv"
df = pd.read_csv(url)

planet_counts = df['hostname'].value_counts()
multi_planet_stars = planet_counts[planet_counts > 1].index
df_multi = df[df['hostname'].isin(multi_planet_stars)]

G = nx.Graph()
for _, row in df_multi.iterrows():
  G.add_edge(row['hostname'], row['pl_name'])

pos = nx.spring_layout(G, iterations=50, seed=42)
nx.draw(G, pos, with_labels=True, font_size=8, node_color='red', node_size=200, edge_color='gray', alpha=0.7)
plt.title("Real NASA multi-planet systems network(Host Stars and Planet)")
print("Number of exoplanets (in multi-planet systems):", len(df_multi))
print("Most planetary system:", df_multi['hostname'].value_counts().idxmax(), "with", df_multi['hostname'].value_counts().max(), "planets")
plt.show()
input("Press Enter to close...")
