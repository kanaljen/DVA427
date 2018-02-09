# Author: Aric Hagberg (hagberg@lanl.gov)
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

fname = 'city.txt'
dt = np.dtype('str, str, uint8')

dataset = np.loadtxt(fname, dtype='str', skiprows=3)

G = nx.Graph()

for line in range(dataset.shape[0]):
	A = dataset[line][0]
	B = dataset[line][1]
	C = dataset[line][2]
	G.add_edge(A,B,weight=int(C))


pos = nx.spring_layout(G)  # positions for all nodes

labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

# nodes
nx.draw_networkx_nodes(G, pos, node_color='black', node_size=500)

# edges
nx.draw_networkx_edges(G, pos, width=2, edge_color='black')

# labels
nx.draw_networkx_labels(G, pos, font_size=15, font_family='sans-serif',font_color='white')

plt.axis('off')
plt.show()