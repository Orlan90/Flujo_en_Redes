import networkx as nx
import matplotlib.pyplot as plt

MDR = nx.MultiDiGraph()

MDR.add_nodes_from(["D1","D5"])
MDR.add_edges_from([("D1","D2"),("D1","D4"),("D2","D3"),("D3","D2"),("D3","D4"),("D3","D5"),("D4","D5"),
                    ("D5","D5")])

nx.draw(MDR, node_size = 1000, node_color = 'y', node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("MDR.eps")
plt.show()