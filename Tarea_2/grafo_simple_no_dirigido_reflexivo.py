import networkx as nx
import matplotlib.pyplot as plt

GNDR = nx.Graph()

GNDR.add_nodes_from(["C1","C7"])
GNDR.add_edges_from([("C1","C2"),("C2","C3"),("C3","C4"),("C4","C5"),("C5","C3"),("C3","C6"),
                     ("C6","C7"),("C7","C7")])

color_map = []
for node in GNDR:
    if (node == "C7"):
        color_map.append('blue')
    else:
        color_map.append('red')

layout = nx.kamada_kawai_layout(GNDR)

nx.draw(GNDR, pos=layout, node_size = 1000, node_color = color_map, node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("GNDR.eps")
plt.show()
