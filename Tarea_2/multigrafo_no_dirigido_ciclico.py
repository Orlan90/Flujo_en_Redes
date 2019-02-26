import networkx as nx
import matplotlib.pyplot as plt

MNDC = nx.MultiGraph()
MNDC.add_nodes_from(["1","9"])

MNDC.add_edges_from([("1","2")], color='lightblue', weight=8)
MNDC.add_edges_from([("2","3"),("3","4"),("4","5"),("5","6"),("6","7"),("7","8"),("8","9"),
                     ("2","1"),("1","6"),("2","7"),("4","9")], color='black', weight=2)

edges = MNDC.edges()

colors = []
weight = []

for (u,v,attrib_dict) in list(MNDC.edges.data()):
    colors.append(attrib_dict['color'])
    weight.append(attrib_dict['weight'])

color_map = []
for node in MNDC:
    if (node == "1" or node == "2"):
        color_map.append('blue')
    else:
        color_map.append('red')

nx.draw_circular(MNDC, edges=edges, edge_color=colors, width=weight, node_size = 1000,
                 node_color = color_map, node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("MNDC.eps")
plt.show()