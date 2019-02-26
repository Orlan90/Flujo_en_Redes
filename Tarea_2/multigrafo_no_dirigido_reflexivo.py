import networkx as nx
import matplotlib.pyplot as plt

MNDR = nx.MultiGraph()

MNDR.add_nodes_from(["1","5"])
MNDR.add_edges_from([("1","2"),("2","3"),("2","4"),("2","5"),("3","5"),("4","5"),("3","5"), ("4","5"),("5","5")])

color_map = []
for node in MNDR:
    if (node == "5"):
        color_map.append('yellow')
    else:
        color_map.append('red')

nx.draw_spectral(MNDR, node_size = 1000, node_color = color_map, node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("MNDR.eps")
plt.show()