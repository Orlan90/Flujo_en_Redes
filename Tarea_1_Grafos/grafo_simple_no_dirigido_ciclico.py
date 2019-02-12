import networkx as nx
import matplotlib.pyplot as plt

GNDC = nx.Graph()

GNDC.add_node("F")
GNDC.add_nodes_from(["C1","C2","C3","C4"])

GNDC.add_edges_from([("F","C3"),("C3","C4"),("C4","C2"),("C2","C1"),("C1","F")])

nx.draw_spectral(GNDC, node_size = 2000, node_color = 'y', node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("GNDC.eps")
plt.show()