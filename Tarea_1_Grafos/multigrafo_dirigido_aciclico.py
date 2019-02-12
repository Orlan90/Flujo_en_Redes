import networkx as nx
import matplotlib.pyplot as plt

MDA = nx.MultiDiGraph()

MDA.add_nodes_from(["C1","C5"])
MDA.add_edges_from([("C1","C3"),("C2","C3"),("C3","C4"),("C3","C4"),("C4","C5")])

nx.draw_spectral(MDA, node_size = 1000, node_color = 'y', node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("MDA.eps")
plt.show()