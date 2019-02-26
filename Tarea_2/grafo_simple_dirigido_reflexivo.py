import networkx as nx
import matplotlib.pyplot as plt

GDR = nx.DiGraph()

GDR.add_nodes_from(["C1","C5"])
GDR.add_edges_from([("C1","C2"),("C2","C3"),("C3","C4"),("C4","C2"),("C5","C1"),("C5","C5")])

color_map = []
for node in GDR:
    if (node == "C5"):
        color_map.append('blue')
    else:
        color_map.append('red')

nx.draw_shell(GDR, node_size = 2000, node_color = color_map, node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("GDR.eps")
plt.show()