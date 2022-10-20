import numpy as np
import matplotlib.pyplot as plt

m=1
mu=0
g=9.81
l=2

def dyn_pendule (X, u):
    x1_dot=X[1]
    x2_dot=-g*np.sin(X[0])+(-mu*X[1]+u)/(m*l)
    return np.array([x1_dot, x2_dot])

h=1e-3 #attention au pas de temps
T=np.arange(0, 100, h) #100 secondes
Xeuler=np.array([1, 0]) #etat initial
XRK2=np.array([1, 0])

etats_euler=[Xeuler]
etats_RK2=[XRK2]
u=0


for t in (T):
    Xeuler=Xeuler+h*dyn_pendule(Xeuler, u)
    etats_euler.append(Xeuler)

    k1=dyn_pendule(XRK2, u)
    k2=dyn_pendule(X RK2+(h*k1), u)
    XRK2=XRK2+(h/2)*(k1+k2)
    etats_RK2.append((XRK2))


etats_euler=np.array(etats_euler)[:-1] # on enléve le dernier éléments comme on il y a un arg en trop à cause du for
etats_RK2=np.array(etats_RK2)[:-1] # on enléve le dernier éléments comme on il y a un arg en trop à cause du for



plt.subplot(121)
plt.plot(T, etats_euler[:, 0], '-r', label="euler")
plt.legend()
plt.subplot(122)
plt.plot(T, etats_RK2[:, 0], 'tab:orange', label="RK2")
plt.legend()
plt.show()


plt.figure()
plt.subplot(121)
plt.plot(etats_euler[:, 0], etats_euler[:, 1], '-r', label="euler")
plt.legend()
plt.subplot(122)
plt.plot(etats_RK2[:, 0], etats_RK2[:, 1], 'tab:orange', label="RK2")
plt.legend()
plt.show()






