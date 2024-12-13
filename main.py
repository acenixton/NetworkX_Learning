import networkx as nx
import matplotlib.pyplot as plt
# from person import *

edgelist = [(1,2,1.0),(2,3,1.5),(4,5,2.5)]
G = nx.Graph()
G.add_weighted_edges_from(edgelist)

nx.draw(G, with_labels=True)

plt.show()

