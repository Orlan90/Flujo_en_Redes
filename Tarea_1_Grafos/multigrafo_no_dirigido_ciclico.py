import networkx as nx
import matplotlib.pyplot as plt

MNDC = nx.MultiGraph()

MNDC.add_nodes_from(["1","9"])
MNDC.add_edges_from([("1","2"),("2","3"),("3","4"),("4","5"),("5","6"),("6","7"),("7","8"),("8","9"),
                     ("2","1"),("1","6"),("2","7"),("4","9")])

nx.draw_circular(MNDC, node_size = 1000, node_color = 'y', node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("MNDC.eps")
plt.show()