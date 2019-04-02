import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from time import time
from networkx.algorithms.flow import maximum_flow_value
from networkx.algorithms.flow import minimum_cut
from networkx.algorithms.flow import minimum_cut_value
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

'''
start_time = time()
elapsed_time = time() - start_time
print("Elapsed_time: %.10f seconds." % elapsed_time)
'''

misdatos = pd.DataFrame()

sources = [2,3,4,5,6]
sinks = [4,2,3,1,0]
for nodes in range(5):
    for k in range(10):
        for l in range(3,7):
            l = 2 ** l
            #print(l)

            #PRIMER GENERADOR

            tiempo = time()
            F = nx.full_rary_tree(2, l)
            w = norm.rvs(10.0, 0.5, nx.number_of_edges(F))
            mu, std = norm.fit(w)
            m = 0
            for u,v,d in F.edges(data=True):
                d['weight'] = w[m]
                m += 1
            tiempo = time() - tiempo

            tiempoalgo = time()
            for a in range(5):
                flow_value = maximum_flow_value(F, sources[nodes], sinks[nodes], capacity='weight')
            tiempoalgo = time() - tiempoalgo + tiempo

            row = pd.DataFrame({'Generador': ['Árbol lleno r-ario'], 'Algoritmo': ['Valor de flujo máximo'],
                                'Orden': len(F),'Densidad': F.size()/nx.complete_graph(l).size(),
                                'Tiempo': tiempoalgo})
            misdatos = misdatos.append(row)

            tiempoalgo = time()
            for a in range(5):
                m_cut = minimum_cut(F, sources[nodes], sinks[nodes], capacity='weight')
            tiempoalgo = time() - tiempoalgo + tiempo

            row = pd.DataFrame({'Generador': ['Árbol lleno r-ario'], 'Algoritmo': ['Corte mínimo'],
                                'Orden': len(F), 'Densidad': F.size() / nx.complete_graph(l).size(),
                                'Tiempo': tiempoalgo})
            misdatos = misdatos.append(row)

            tiempoalgo = time()
            for a in range(5):
                cut_value = minimum_cut_value(F, sources[nodes], sinks[nodes], capacity='weight')
            tiempoalgo = time() - tiempoalgo + tiempo

            row = pd.DataFrame({'Generador': ['Árbol lleno r-ario'], 'Algoritmo': ['Valor de corte mínimo'],
                                'Orden': len(F), 'Densidad': F.size() / nx.complete_graph(l).size(),
                                'Tiempo': tiempoalgo})
            misdatos = misdatos.append(row)

            #SEGUNDO GENERADOR

            tiempo = time()
            G = nx.complete_graph(l)
            w = norm.rvs(10.0, 0.5, nx.number_of_edges(G))
            mu, std = norm.fit(w)
            m = 0
            for u, v, d in G.edges(data=True):
                d['weight'] = w[m]
                m += 1
            tiempo = time() - tiempo

            tiempoalgo = time()
            for a in range(5):
                flow_value = nx.maximum_flow_value(G, sources[nodes], sinks[nodes], capacity='weight')
            tiempoalgo = time() - tiempoalgo + tiempo

            row = pd.DataFrame({'Generador': ['Grafo completo'], 'Algoritmo': ['Valor de flujo máximo'],
                                'Orden': len(G),'Densidad': G.size() / nx.complete_graph(l).size(),
                                'Tiempo': tiempoalgo})
            misdatos = misdatos.append(row)

            tiempoalgo = time()
            for a in range(5):
                m_cut = nx.minimum_cut(G, sources[nodes], sinks[nodes], capacity='weight')
            tiempoalgo = time() - tiempoalgo + tiempo

            row = pd.DataFrame({'Generador': ['Grafo completo'], 'Algoritmo': ['Corte mínimo'], 'Orden': len(G),
                                'Densidad': G.size() / nx.complete_graph(l).size(), 'Tiempo': tiempoalgo})
            misdatos = misdatos.append(row)

            tiempoalgo = time()
            for a in range(5):
                cut_value = nx.minimum_cut_value(G, sources[nodes], sinks[nodes], capacity='weight')
            tiempoalgo = time() - tiempoalgo + tiempo

            row = pd.DataFrame({'Generador': ['Grafo completo'], 'Algoritmo': ['Valor de corte mínimo'],
                                'Orden': len(G), 'Densidad': G.size() / nx.complete_graph(l).size(),
                                'Tiempo': tiempoalgo})
            misdatos = misdatos.append(row)

            #TERCER GENERADOR

            tiempo = time()
            H = nx.wheel_graph(l)
            w = norm.rvs(10.0, 0.5, nx.number_of_edges(H))
            mu, std = norm.fit(w)
            m = 0
            for u, v, d in H.edges(data=True):
                d['weight'] = w[m]
                m += 1
            tiempo = time() - tiempo

            tiempoalgo = time()
            for a in range(5):
                flow_value = nx.maximum_flow_value(H, sources[nodes], sinks[nodes], capacity='weight')
            tiempoalgo = time() - tiempoalgo + tiempo

            row = pd.DataFrame({'Generador': ['Grafo rueda'], 'Algoritmo': ['Valor de flujo máximo'],
                                'Orden': len(H),'Densidad': H.size() / nx.complete_graph(l).size(),
                                'Tiempo': tiempoalgo})
            misdatos = misdatos.append(row)

            tiempoalgo = time()
            for a in range(5):
                m_cut = nx.minimum_cut(H, sources[nodes], sinks[nodes], capacity='weight')
            tiempoalgo = time() - tiempoalgo + tiempo

            row = pd.DataFrame({'Generador': ['Grafo rueda'], 'Algoritmo': ['Corte mínimo'], 'Orden': len(H),
                                'Densidad': H.size() / nx.complete_graph(l).size(), 'Tiempo': tiempoalgo})
            misdatos = misdatos.append(row)

            tiempoalgo = time()
            for a in range(5):
                cut_value = nx.minimum_cut_value(H, sources[nodes], sinks[nodes], capacity='weight')
            tiempoalgo = time() - tiempoalgo + tiempo

            row = pd.DataFrame({'Generador': ['Grafo rueda'], 'Algoritmo': ['Valor de corte mínimo'],
                                'Orden': len(H), 'Densidad': H.size() / nx.complete_graph(l).size(),
                                'Tiempo': tiempoalgo})
            misdatos = misdatos.append(row)

graf_1 = sns.boxplot(x ='Generador', y = 'Tiempo', data = misdatos, hue = 'Generador')
plt.ylabel('Tiempo (ms)')
plt.savefig('graf_1.eps')
plt.show()

graf_2 = sns.boxplot(x ='Algoritmo', y = 'Tiempo', data = misdatos, hue = 'Algoritmo')
plt.ylabel('Tiempo (ms)')
plt.savefig('graf_2.eps')
plt.show()

graf_3 = sns.boxplot(x ='Orden', y = 'Tiempo', data = misdatos, hue = 'Orden')
plt.ylabel('Tiempo (ms)')
plt.savefig('graf_3.eps')
plt.show()

graf_4 = sns.boxplot(x ='Densidad', y = 'Tiempo', data = misdatos, hue = 'Generador')
plt.ylabel('Tiempo (ms)')
plt.savefig('graf_4.eps')
plt.show()

model = ols('Tiempo ~ Generador + Orden + Algoritmo + Densidad + Generador*Orden + Generador*Algoritmo + Generador*Densidad + Orden*Algoritmo + Orden*Densidad + Algoritmo*Densidad',\
            data = misdatos).fit()

ANOVA = sm.stats.anova_lm(model, typ=2)
print(ANOVA)

for i in range(len(ANOVA)):
    print("{:s} {:s} es significativo".format(ANOVA.index[i], "" if ANOVA['PR(>F)'][i] < 0.05 else "no es significativo"))

#print(misdatos)