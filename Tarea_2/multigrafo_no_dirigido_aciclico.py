import networkx as nx
from fa2 import ForceAtlas2
import matplotlib.pyplot as plt

MNDA = nx.MultiGraph()

MNDA.add_nodes_from(["S1", "S5"])
MNDA.add_edges_from([("S3", "S4"), ("S4", "S5")], color='blue', weight=5)
MNDA.add_edges_from([("S1", "S2"), ("S2", "S3"), ("S2", "S4"), ("S2", "S5"), ("S3", "S4"),
                     ("S4", "S5"),("S3", "S5")], color='black', weight=2)

edges = MNDA.edges()
colors = []
weight = []
for (u, v, attrib_dict) in list(MNDA.edges.data()):
    colors.append(attrib_dict['color'])
    weight.append(attrib_dict['weight'])

#Tomado de: https://github.com/bhargavchippada/forceatlas2/blob/master/README.md
forceatlas2 = ForceAtlas2(
    outboundAttractionDistribution=True,
    linLogMode=False,
    adjustSizes=False,
    edgeWeightInfluence=1.0,

    jitterTolerance=1.0,
    barnesHutOptimize=True,
    barnesHutTheta=1.2,
    multiThreaded=False,

    scalingRatio=2.0,
    strongGravityMode=False,
    gravity=1.0,

    verbose=True)

positions = forceatlas2.forceatlas2_networkx_layout(MNDA, pos=None, iterations=1000)
nx.draw_networkx_nodes(MNDA, positions, node_size=500, with_labels=False, node_color="blue", alpha=0.4)
nx.draw_networkx_edges(MNDA, positions, edge_color="black", alpha=0.05)
plt.axis('off')
plt.savefig("MNDA.eps")
plt.show()

