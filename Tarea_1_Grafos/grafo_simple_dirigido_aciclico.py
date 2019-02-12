import networkx as nx
import matplotlib.pyplot as plt

GDA = nx.DiGraph()

GDA.add_nodes_from(["E1","E7"])
GDA.add_edges_from([("E1","E2"),("E1","E3"),("E2","E4"),("E2","E5"),("E3","E6"),("E3","E7")])

nx.draw(GDA, node_size = 2000, node_color = 'y', node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("GDA.eps")
plt.show()

