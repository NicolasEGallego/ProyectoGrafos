from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx

class Estrella:
    def __int__(self,mag,dist):
        self.mag=mag
        self.dist=dist


Acuario = nx.Graph()
Vertices_acu = ['ε','µ','β','α','π','ζ','γ','θ','ρ','λ','η','ι','ξ','δ','ϕ','τ','88','ψ']
Acuario.add_nodes_from(Vertices_acu)
Aristas_acu = [('ε','µ'),('µ','β'),('β','α'),('β','ξ'),('α','π'),('α','γ'),('α','θ'),('π','ζ'),('ζ','γ'),
               ('ζ','η'),('θ','ρ'),('ρ','λ'),('λ','ϕ'),('λ','τ'),('ι','ξ'),('δ','τ'),('δ','ψ'),('ϕ','ψ'),('88','ψ')]
Acuario.add_edges_from(Aristas_acu)

ubica2={'ε':(8.4,2.3),'µ':(7.95,2.55),'β':(6,3.35),'α':(4.25,4.45),'π':(3.25,4.8),'ζ':(3.025,4.5),
       'γ':(3.45,4.25),'θ':(5.2,2.95),'ρ':(4.8,2.95),'λ':(1.9,2.9),'η':(2.6,4.5),'ι':(4.2,1.7),'ξ':(5.7,2.9),
       'δ':(1.85,1.3),'ϕ':(0.75,3.4),'τ':(2.1,1.75),'88':(1.15,0.15),'ψ':(0.65,2.55)}

epsilon = Estrella()
epsilon.mag=3.77
epsilon.dist=229.42

mu=Estrella()
mu.mag=4.73
mu.dist=155.16


beta =Estrella()
beta.mag=2.91
beta.dist=611.63


alpha=Estrella()
alpha.mag=2.96
alpha.dist=758.14


pi=Estrella()
pi.mag=4.66
pi.dist=1101.35

zeta=Estrella()
zeta.mag=4.59
zeta.dist=103.39

gamma=Estrella()
gamma.mag=3.84
gamma.dist=157.72

theta=Estrella()
theta.mag=4.16
theta.dist=191.31

rho=Estrella()
rho.mag=5.37
rho.dist=742.60

lamb=Estrella()
lamb.mag=3.74
lamb.dist=391.36

eta=Estrella()
eta.mag=4.02
eta.dist=183.46

iota=Estrella()
iota.mag=4.27
iota.dist=172.49

xi=Estrella()
xi.mag=4.69
xi.dist=178.53

delta=Estrella()
delta.mag=3.27
delta.dist=159.49

phi=Estrella()
phi.mag=4.22
phi.dist=222.07

tao=Estrella()
tao.mag=4.01
tao.dist=379.95

a88=Estrella()
a88.mag=3.66
a88.dist=233.52

psi=Estrella()
psi.mag=4.21
psi.dist=148.38

acumag = epsilon.mag + mu.mag + beta.mag + alpha.mag + pi.mag + zeta.mag + gamma.mag + theta.mag + rho.mag + lamb.mag + eta.mag + iota.mag + xi.mag + delta.mag + phi.mag + tao.mag + a88.mag + psi.mag
print(acumag)

acudist = (epsilon.dist + mu.dist + beta.dist + alpha.dist + pi.dist + zeta.dist + gamma.dist + theta.dist + rho.dist + lamb.dist + eta.dist + iota.dist + xi.dist + delta.dist + phi.dist + tao.dist + a88.dist + psi.dist)/len(Vertices_acu)
print(acudist)

nx.draw(Acuario, pos=ubica2, node_color='cyan', edge_color='black', with_labels=True)

plt.show()