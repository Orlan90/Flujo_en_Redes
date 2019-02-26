import networkx as nx
import matplotlib.pyplot as plt

GNDA = nx.Graph()

GNDA.add_node("Gerente")
GNDA.add_nodes_from(["Subgerente","Asistente","Coordinador","Planificador","Organizador","Supervisor"])

GNDA.add_edges_from([("Gerente","Subgerente"),("Subgerente","Asistente")])
GNDA.add_edges_from([("Asistente","Coordinador"),("Asistente","Planificador")])
GNDA.add_edges_from([("Asistente","Organizador"),("Asistente","Supervisor")])

nx.draw_spring(GNDA, node_size = 5500, node_color = 'y', node_shape = 's', with_labels=True)
plt.draw()
plt.savefig("GNDA.eps")
plt.show()