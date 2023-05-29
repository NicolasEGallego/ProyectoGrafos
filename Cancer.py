from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx


Cancer = nx.Graph()
Vertices_can = ['α','β','γ','δ', 'ι']
Cancer.add_nodes_from(Vertices_can)
Aristas_can = [('ι','γ'),('γ','δ'),('δ','α'),('δ','β')]
Cancer.add_edges_from(Aristas_can)

ubica4={'β':(4.5,0.25),'α':(0.5,1.95),'γ':(2.05,5.05),'δ':(1.9,3.75),'ι':(1.85,7.85)}

nx.draw(Cancer, pos=ubica4, node_color='crimson', edge_color='black', with_labels=True)

plt.show()