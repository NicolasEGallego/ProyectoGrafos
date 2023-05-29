from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx

class Estrella:
    def __int__(self,mag,dist):
        self.mag = mag
        self.dist = dist

Sagitario = nx.Graph()
Vertices_sag = ['µ', 'λ', 'ϕ', 'δ', 'γ', 'ε', 'σ', 'η', 'τ', 'ζ']
Sagitario.add_nodes_from(Vertices_sag)
Aristas_sag = [('µ','λ'),('λ','ϕ'),('λ','δ'),('ϕ','δ'),('ϕ','σ'),('ϕ','ζ'),('δ','γ'),('δ','ε'),('γ','ε'),
               ('ε','η'),('ε','ζ'),('σ','τ'),('τ','ζ')]
Sagitario.add_edges_from(Aristas_sag)

ubica1={'µ':(6.3,7.45),'λ':(4.65,5.55),'ϕ':(2.75,4.9),'δ':(5.2,3.45),'γ':(6.7,3),'ε':(4.75,1.35),
       'σ':(1.75,5.25),'η':(5.25,0.2),'τ':(0.55,4.6),'ζ':(1,3.6)}

mu = Estrella()
mu.mag = 3.86
mu.dist = 29636.36

lamb = Estrella()
lamb.mag = 2.81
lamb.dist = 77.25

phi = Estrella()
phi.mag = 3.17
phi.dist = 230.55

delta = Estrella()
delta.mag = 2.7
delta.dist = 35.53

gamma = Estrella()
gamma.mag = 2.99
gamma.dist = 96.05

epsilon = Estrella()
epsilon.mag = 1.85
epsilon.dist = 144.57

sigma = Estrella()
sigma.mag = 2.02
sigma.dist = 224.21

eta = Estrella()
eta.mag = 3.11
eta.dist = 149.06

tau =Estrella()
tau.mag = 3.32
tau.dist = 120.34

zeta = Estrella()
zeta.mag = 2.6
zeta.dist = 89.05

sagimag = mu.mag + lamb.mag + phi.mag + delta.mag + gamma.mag + epsilon.mag + sigma.mag + eta.mag + tau.mag + zeta.mag
print(sagimag)

sagidist = (mu.dist + lamb.dist + phi.dist + delta.dist + gamma.dist + epsilon.dist + sigma.dist + eta.dist + tau.dist + zeta.dist)/len(Vertices_sag)
print(sagidist)

A = nx.draw(Sagitario, pos=ubica1, node_color='b', edge_color='black', with_labels=True)

plt.show()