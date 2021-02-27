import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#Import Data
data1 = pd.read_excel('raan_case_study.xlsx', header=0, sheet_name=0)
data2 = pd.read_excel('raan_case_study.xlsx', header=0, sheet_name=1)
sourse_id = data1.iloc[:, 0].values.tolist()
target_id = data1.iloc[:, 1].values.tolist()
weights = data1.iloc[:, 2].values.tolist()
edges = list(zip(sourse_id, target_id, weights))
ids_to_rename = data2.iloc[:, 0].values.tolist()
labels_new = data2.iloc[:, 2].values.tolist()
colors = data2.iloc[:, 3].values.tolist()

#Create graph and add weights
G = nx.Graph()
G.add_weighted_edges_from(edges)
dicts = {}
for i, x in zip(ids_to_rename, labels_new):
    dicts[i] = x
color_map = []
for k, node in enumerate(ids_to_rename):
    color_map.append(colors[k])


#Plot the graph
H = nx.relabel_nodes(G, dicts)
plt.figure(3, figsize=(14, 14))
pos = nx.spring_layout(H)
nx.draw_networkx(H, pos, node_size=1800, node_color=color_map, font_size=10)
labels = nx.get_edge_attributes(H, 'weight')
nx.draw_networkx_edge_labels(H, pos, edge_labels=labels)
plt.show()
