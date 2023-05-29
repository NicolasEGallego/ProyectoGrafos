from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx

Libra = nx.Graph()
Vertices_lib = ['α','β','γ','σ','υ','τ']
Libra.add_nodes_from(Vertices_lib)
Aristas_lib = [('β','γ'),('β','α'),('γ','α'),('γ','υ'),('α','σ'),('υ','τ')]
Libra.add_edges_from(Aristas_lib)

ubica7={'α':(4.45,5),'β':(2.25,7.35),'γ':(0.65,5.45),'σ':(3.25,1.8),'υ':(0.65,0.85),'τ':(0.525,0.25)}

nx.draw(Libra, pos=ubica7, node_color='sienna', edge_color='black', with_labels=True)

plt.show()