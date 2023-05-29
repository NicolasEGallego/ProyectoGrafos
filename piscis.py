from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx

Piscis = nx.Graph()
Vertices_pis = ['α','γ','υ','τ','ϕ','η','ο','ν','ε','δ','ω','ι','θ','κ','λ','μ']
Piscis.add_nodes_from(Vertices_pis)
Aristas_pis = [('τ','υ'),('τ','ϕ'),('υ','ϕ'),('ϕ','η'),('η','ο'),('ο','α'),('α','ν'),('ν','μ'),('ε','δ'),('ε','μ'),('δ','ω'),
               ('ω','ι'),('ι','θ'),('ι','λ'),('θ','γ'),('γ','κ'),('κ','λ')]
Piscis.add_edges_from(Aristas_pis)

ubica8={'α':(0.4,1),'γ':(12.15,1.1),'υ':(3.75,7.7),'τ':(4.3,8.45),'ϕ':(4.1,6.9),'η':(2.8,4.35),'ο':(1.7,2.7),'ν':(1.92,1.65),'ε':(4.65,2.15),'δ':(5.65,2.1),'ω':(9.1,1.9),'ι':(10.5,1.6),'θ':(11.35,1.9),'κ':(11.5,0.45),'λ':(10.4,0.55),'μ':(2.72,1.8)}

nx.draw(Piscis, pos=ubica8, node_color='teal', edge_color='black', with_labels=True)

plt.show()