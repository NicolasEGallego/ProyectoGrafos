from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx

Capricornio = nx.Graph()
Vertices_cap = ['δ','γ','θ','α','β','ο','ω','ζ','ε','ψ','ν','24']
Capricornio.add_nodes_from(Vertices_cap)
Aristas_cap = [('δ','γ'),('δ','ε'),('γ','θ'),('θ','ν'),('α','β'),('α','ν'),('β','ο'),('ο','ψ'),('ω','ψ'),('ω','24'),('ζ','ε'),('ζ','24')]
Capricornio.add_edges_from(Aristas_cap)

ubica11={'δ':(0.55,3.9),'γ':(1.15,3.75),'θ':(3.92,3.65),'α':(7.9,5.12),'β':(7.6,4.37),'ο':(6.85,3.15),'ω':(5.2,0.35),'ζ':(2.3,1.85),'ε':(1.42,2.8),'ψ':(5.45,0.9),'ν':(7.7,5.1),'24':(3.85,1)}

nx.draw(Capricornio, pos=ubica11, node_color='brown', edge_color='black', with_labels=True)

plt.show()