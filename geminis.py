from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx

Geminis = nx.Graph()
Vertices_gem = ['α','β','γ','δ','ι','ξ','λ','ζ','κ','υ','τ','θ','ε','ν','µ','η']
Geminis.add_nodes_from(Vertices_gem)
Aristas_gem = [('γ','ζ'),('ξ','λ'),('λ','δ'),('ζ','δ'),('δ','υ'),('κ','υ'),('υ','β'),('υ','ι'),('ι','τ'),('τ','α'),('τ','θ'),('τ','ε'),('ε','ν'),('ε','µ'),('η','µ')]
Geminis.add_edges_from(Aristas_gem)

ubica5={'β':(0.55,6.1),'α':(1.5,7.4),'γ':(5.95,1.75),'δ':(2.4,3.8),'ι':(2.075,5.9),'ξ':(5.3,0.5),'λ':(2.5,1.85),'ζ':(3.75,3.25),'κ':(0.5,4.8),'υ':(1.5,5.6),
       'τ':(3.25,6.7),'θ':(4.7,8),'ε':(5.4,4.9),'ν':(6.65,3.1),'µ':(7.15,4),'η':(7.8,4)}

nx.draw(Geminis, pos=ubica5, node_color='chartreuse', edge_color='black', with_labels=True)

plt.show()