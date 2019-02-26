import networkx as nx
import matplotlib.pyplot as plt

GDC = nx.DiGraph()

GDC.add_nodes_from(["S1","S5"])
GDC.add_edges_from([("S1","S2"),("S2","S5"),("S3","S4"),("S4","S5"),("S5","S1")])

nx.draw_spring(GDC, node_size = 1000, node_color = 'y', node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("GDC.eps")
plt.show()