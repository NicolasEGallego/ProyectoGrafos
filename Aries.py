from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx

Aries = nx.Graph()
Vertices_ari = ['α','β','γ','41']
Aries.add_nodes_from(Vertices_ari)
Aristas_ari = [('41','α'),('α','β'),('β','γ')]
Aries.add_edges_from(Aristas_ari)

ubica3={'β':(7.4,1.4),'α':(5.75,2.75),'γ':(7.6,0.6),'41':(0.4,4.75)}

nx.draw(Aries, pos=ubica3, node_color='grey', edge_color='black', with_labels=True)

plt.show()