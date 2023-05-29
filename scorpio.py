from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx

class Estrella:
    def __int__(self,mag,dist):
        self.mag = mag
        self.dist = dist

Scorpio = nx.Graph()
Vertices_sco = ['λ','υ','κ','ι','θ','η','ζ','μ','ε','τ','α','σ','δ','β','π','ρ','ν']
Scorpio.add_nodes_from(Vertices_sco)
Aristas_sco = [('λ','υ'),('λ','κ'),('κ','ι'),('ι','θ'),('θ','η'),('η','ζ'),('ζ','μ'),('μ','ε'),('ε','τ'),('τ','α'),('α','σ'),('σ','ρ'),('σ','ν'),('δ','β'),('β','ν'),('π','ρ')]
Scorpio.add_edges_from(Aristas_sco)

ubica9={'λ':(1.35,3.3),'υ':(1.7,3.2),'κ':(0.75,2.4),'ι':(0.4,1.9),'θ':(1.35,0.85),'η':(3.25,0.95),'ζ':(4.5,1.35),'μ':(4.7,3.1),'ε':(4.85,4.6),'τ':(6.1,7),'α':(6.75,7.7),'σ':(7.5,8),'δ':(9.6,9.1),'β':(9.25,10.35),'π':(9.55,7.65),'ρ':(9.55,6.35),'ν':(8.6,10.55)}

lamb = Estrella()
lamb.mag = 1.63
lamb.dist=702.59

upsilon = Estrella()
upsilon.mag = 2.69
upsilon.dist=518.28

kappa = Estrella()
kappa.mag = 2.41
kappa.dist = 463.73

iota = Estrella()
iota.mag = 3.03
iota.dist=1791.21

theta = Estrella()
theta.mag = 1.87
theta.dist = 271.89

eta = Estrella()
eta.mag=3.33
eta.dist=71.55

zeta = Estrella()
zeta.mag=3.62
zeta.dist=150.44

mu = Estrella()
mu.mag = 3.08
mu.dist=821.16

epsilon = Estrella()
epsilon.mag=2.29
epsilon.dist=65.40

tau = Estrella()
tau.mag=2.82
tau.dist=429.51

alpha = Estrella()
alpha.mag=0.96
alpha.dist=603.70

sigma = Estrella()
sigma.mag=2.89
sigma.dist=734.23

delta = Estrella()
delta.mag = 2.32
delta.dist=401.48

beta = Estrella()
beta.mag = 2.62
beta.dist = 530.08

pi = Estrella()
pi.mag = 2.89
pi.dist = 459.15

rho = Estrella()
rho.mag = 3.88
rho.dist = 409.03

nu = Estrella()
nu.mag = 4.01
nu.dist=436.41

scomag = lamb.mag + upsilon.mag + kappa.mag + iota.mag + theta.mag + eta.mag + zeta.mag + mu.mag + epsilon.mag + tau.mag + alpha.mag + sigma.mag + delta.mag + beta.mag + pi.mag + rho.mag + nu.mag
print(scomag)

scodist = (lamb.dist + upsilon.dist + kappa.dist + iota.dist + theta.dist + eta.dist + zeta.dist + mu.dist + epsilon.dist + tau.dist + alpha.dist + sigma.dist + delta.dist + beta.dist + pi.dist + rho.dist + nu.dist)/len(Vertices_sco)
print(scodist)

nx.draw(Scorpio, pos=ubica9, node_color='silver', edge_color='black', with_labels=True)

plt.show()