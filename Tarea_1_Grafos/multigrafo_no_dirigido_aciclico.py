import networkx as nx
import matplotlib.pyplot as plt

MNDA = nx.MultiGraph()

MNDA.add_nodes_from(["S1","S5"])
MNDA.add_edges_from([("S1","S2"),("S2","S3"),("S2","S4"),("S2","S5"),("S3","S4"),("S3","S4"),("S4","S5"),
                     ("S4","S5"),("S3","S5")])

nx.draw(MNDA, node_size = 1000, node_color = 'y', node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("MNDA.eps")
plt.show()

