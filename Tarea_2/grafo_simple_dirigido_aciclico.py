import networkx as nx
import matplotlib.pyplot as plt

GDA = nx.DiGraph()

GDA.add_nodes_from(["E1","E2","E3"], bipartite=0)
GDA.add_nodes_from(["E4","E5","E6","E7"], bipartite=1)

GDA.add_edges_from([("E1","E4"),("E1","E5"),("E2","E6"),("E2","E7"),("E3","E4"),("E3","E7")])

nx.draw(GDA, pos=nx.bipartite_layout(GDA,["E1","E2","E3"]), node_size = 2000, node_color = 'y',
        node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("GDA.eps")
plt.show()

