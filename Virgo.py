from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx

Virgo = nx.Graph()
Vertices_vir = ['α', 'β', 'ε', 'δ', 'γ', 'η', 'ν', 'ο', 'θ', 'ζ', 'τ', 'ι', 'μ', '109']
Virgo.add_nodes_from(Vertices_vir)
Aristas_vir = [('α','θ'),('β','η'),('β','ν'),('ε','δ'),('δ','γ'),('γ','η'),('γ','θ'),('γ','ζ'),('η','ο'),('ν','ο'),('ζ','τ'),('ζ','ι'),
               ('τ','109'),('ι','μ')]
Virgo.add_edges_from(Aristas_vir)

ubica12={'α':(5.8,0.2),'β':(12.2,3.7),'ε':(7.35,6.25),'δ':(7.8,4.2),'γ':(8.75,2.85),'η':(10.25,3.05),'ν':(12.6,5),'ο':(11.25,5.6),'θ':(6.8,1.75),
       'ζ':(5.15,3.1),'τ':(3.3,3.7),'ι':(2.3,1.6),'μ':(0.5,1.65),'109':(0.25,3.75)}

nx.draw(Virgo, pos=ubica12, node_color='g', edge_color='black', with_labels=True)

plt.show()