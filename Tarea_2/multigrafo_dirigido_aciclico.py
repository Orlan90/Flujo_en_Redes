import networkx as nx
import matplotlib.pyplot as plt

MDA = nx.MultiDiGraph()

MDA.add_nodes_from(["C1","C5"])
MDA.add_edges_from([("C3","C4")], color='lightblue', weight=4)
MDA.add_edges_from([("C1","C3"),("C2","C3"),("C3","C4"),("C3","C4"),("C4","C5")], color='black', weight=1)

edges = MDA.edges()

colors = []
weight = []

for (u,v,attrib_dict) in list(MDA.edges.data()):
    colors.append(attrib_dict['color'])
    weight.append(attrib_dict['weight'])

color_map = []
for node in MDA:
    if (node == "C3" or node == "C4"):
        color_map.append('yellow')
    else:
        color_map.append('blue')

frl = nx.fruchterman_reingold_layout(MDA, k=0.40, iterations=40)

nx.draw(MDA, pos=frl, edges=edges, edge_color=colors, width=weight, node_size = 1000,
        node_color = color_map, node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("MDA.eps")
plt.show()