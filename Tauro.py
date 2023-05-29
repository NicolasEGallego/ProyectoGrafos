from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx

Tauro = nx.Graph()
Vertices_tau = ['β','ε','δ','γ','θ','α','ζ','λ','ξ','η','ο']
Tauro.add_nodes_from(Vertices_tau)
Aristas_tau = [('β','ε'),('ε','δ'),('ε','η'),('δ','γ'),('γ','θ'),('γ','λ'),('θ','α'),('α','ζ'),('λ','ξ'),('ξ','ο')]
Tauro.add_edges_from(Aristas_tau)

ubica10={'β':(1.5,6.3),'ε':(5.25,3.3),'δ':(5.6,2.85),'γ':(5.85,2.25),'θ':(5.25,2.35),'α':(4.75,2.55),'ζ':(0.52,4.2),'λ':(7.15,1.45),'ξ':(9.57,0.72),'η':(7.95,4.8),'ο':(9.75,0.5)}

nx.draw(Tauro, pos=ubica10, node_color='orangered', edge_color='black', with_labels=True)

plt.show()