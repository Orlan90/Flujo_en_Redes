import networkx as nx
import matplotlib.pyplot as plt

MDC = nx.MultiDiGraph()

MDC.add_nodes_from(["E1","E5"])
MDC.add_edges_from([("E1","E2"),("E2","E1"),("E2","E3"),("E3","E2"),("E3","E4"),("E4","E3"),
                    ("E4","E5"),("E5","E4")])

nx.draw_spectral(MDC, node_size = 1000, node_color = 'yellow', node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("MDC.eps")
plt.show()