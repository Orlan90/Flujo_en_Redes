import networkx as nx
import matplotlib.pyplot as plt
from time import time
import numpy as np
from scipy import stats


print('topological_sort algorithm')

#Grafo 1

GDA = nx.DiGraph()

GDA.add_nodes_from(["E1","E2","E3"], bipartite=0)
GDA.add_nodes_from(["E4","E5","E6","E7"], bipartite=1)

GDA.add_edges_from([("E1","E4"),("E1","E5"),("E2","E6"),("E2","E7"),("E3","E4"),("E3","E7")])

replicas = []
for j in range(30):
    start_time = time()
    for i in range (100000):
        t_s = nx.topological_sort(GDA)
    elapsed_time = time() - start_time
    replicas.append(elapsed_time)
print(replicas)
print(len(replicas))

normality_test=stats.shapiro(replicas)
print(normality_test)

hist, bin_edges=np.histogram(replicas_f1,density=True)
first_edge, last_edge = np.min(replicas_f1),np.max(replicas_f1)

n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)

plt.hist(replicas_f1, bins=bin_edges, rwidth=0.8, color='orange')
plt.ylabel('Frecuencia')
plt.xlabel('Tiempo (s)')
plt.grid(axis='y', alpha= 0.5)
plt.savefig("Histograma1.eps")
plt.show()

nx.draw(GDA, pos=nx.bipartite_layout(GDA,["E1","E2","E3"]), node_size = 2000, node_color = 'y',
        node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("GDA.eps")
plt.show(1)


print('minimum_spanning_tree algorithm')

#Grafo 2

GNDC = nx.Graph()

GNDC.add_node("F")
GNDC.add_nodes_from(["C1","C2","C3","C4"])

GNDC.add_edge("F","C3", weight = 2)
GNDC.add_edge("C3","C4", weight = 1)
GNDC.add_edge("C4","C2", weight = 4)
GNDC.add_edge("C2","C1", weight = 1)
GNDC.add_edge("C1","F", weight = 2)

replicas_2 = []
for j in range(30):
    start_time = time()
    for i in range (100000):
        mst = nx.minimum_spanning_tree(GNDC)
    elapsed_time = time() - start_time
    replicas_2.append(elapsed_time)
print(replicas_2)
print(len(replicas_2))

normality_test=stats.shapiro(replicas_2)
print(normality_test)

hist, bin_edges=np.histogram(replicas_f2,density=True)
first_edge, last_edge = np.min(replicas_f2),np.max(replicas_f2)

n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)

plt.hist(replicas_f2, bins=bin_edges, rwidth= 0.8, color= 'orange')
plt.ylabel('Frecuencia')
plt.xlabel('Tiempo (s)')
plt.grid(axis='y', alpha= 0.5)
plt.savefig("Histograma2.eps")
plt.show()

g = nx.random_layout(GNDC)

nx.draw(GNDC, node_size = 2000, node_color = 'y', node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("GNDC.eps")
plt.show(2)


print('betweenness_centrality algorithm')

#Grafo 3

GDC = nx.DiGraph()

GDC.add_nodes_from(["S1","S5"])
GDC.add_edges_from([("S1","S2"),("S2","S5"),("S3","S4"),("S4","S5"),("S5","S1")])

replicas_3 = []
for j in range(30):
    start_time = time()
    for i in range (100000):
        b_c = nx.betweenness_centrality(GDC, normalized=False)
    elapsed_time = time() - start_time
    replicas_3.append(elapsed_time)
print(replicas_3)
print(len(replicas_3))

normality_test=stats.shapiro(replicas_3)
print(normality_test)

hist, bin_edges=np.histogram(replicas_f3,density=True)
first_edge, last_edge = np.min(replicas_f3),np.max(replicas_f3)

n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)

plt.hist(replicas_f3, bins=bin_edges, rwidth= 0.8, color= 'orange')
plt.ylabel('Frecuencia')
plt.xlabel('Tiempo (s)')
plt.grid(axis='y', alpha= 0.5)
plt.savefig("Histograma3.eps")
plt.show()

p = nx.spring_layout(GDC)

nx.draw(GDC, node_size = 1000, node_color = 'y', node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("GDC.eps")
plt.show(3)


print('dfs_tree algorithm')

#Grafo 4

GNDA = nx.Graph()

GNDA.add_node("Gerente")
GNDA.add_nodes_from(["Subgerente","Asistente","Coordinador","Planificador","Organizador","Supervisor"])

GNDA.add_edges_from([("Gerente","Subgerente"),("Subgerente","Asistente")])
GNDA.add_edges_from([("Asistente","Coordinador"),("Asistente","Planificador")])
GNDA.add_edges_from([("Asistente","Organizador"),("Asistente","Supervisor")])

replicas_4 = []
for j in range(30):
    start_time = time()
    for i in range (100000):
        dfs = nx.dfs_tree(GNDA)
    elapsed_time = time() - start_time
    replicas_4.append(elapsed_time)
print(replicas_4)
print(len(replicas_4))

normality_test=stats.shapiro(replicas_4)
print(normality_test)

hist, bin_edges=np.histogram(replicas_f4,density=True)
first_edge, last_edge = np.min(replicas_f4),np.max(replicas_f4)

n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)

plt.hist(replicas_f4, bins=bin_edges, rwidth= 0.8, color= 'orange')
plt.ylabel('Frecuencia')
plt.xlabel('Tiempo (s)')
plt.grid(axis='y', alpha= 0.5)
plt.savefig("Histograma4.eps")
plt.show()

p = nx.spring_layout(GNDA)

nx.draw(GNDA, node_size = 5500, node_color = 'y', node_shape = 's', with_labels=True)
plt.draw()
plt.savefig("GNDA.eps")
plt.show(4)


print('max_clique algorithm')

#Grafo 5

MNDR = nx.MultiGraph()

MNDR.add_nodes_from(["1","5"])
MNDR.add_edges_from([("1","2"),("2","3"),("2","4"),("2","5"),("3","5"),("4","5"),("3","5"),
                     ("4","5"),("5","5")])

color_map = []
for node in MNDR:
    if (node == "5"):
        color_map.append('yellow')
    else:
        color_map.append('red')

replicas_5 = []
for j in range(30):
    start_time = time()
    for i in range (100000):
        cliques = nx.cliques_containing_node(MNDR)
    elapsed_time = time() - start_time
    replicas_5.append(elapsed_time)
print(replicas_5)
print(len(replicas_5))

normality_test=stats.shapiro(replicas_5)
print(normality_test)

hist, bin_edges=np.histogram(replicas_f5,density=True)
first_edge, last_edge = np.min(replicas_f5),np.max(replicas_f5)

n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)

plt.hist(replicas_f5, bins=bin_edges, rwidth= 0.8, color= 'orange')
plt.ylabel('Frecuencia')
plt.xlabel('Tiempo (s)')
plt.grid(axis='y', alpha= 0.5)
plt.savefig("Histograma5.eps")
plt.show()

p = nx.spectral_layout(MNDR)

nx.draw(MNDR, node_size = 1000, node_color = color_map, node_shape = 'o', with_labels=True)
plt.draw()
plt.savefig("MNDR.eps")
plt.show(5)