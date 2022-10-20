# import numpy as np
# import matplotlib.pyplot as plt
#
# alpha=beta=1
#
# def dyn_pendule (X, u):
#     x1_dot=(1-alpha*X)*u
#     x2_dot=(-1+beta*u)*X
#     return np.array([x1_dot, x2_dot])
#
# h=1 #attention au pas de temps
# T=np.arange(0, 100, h) #100 secondes
# XRK2=np.array([10, 10])
#
# etats_RK2=[XRK2]
# u=0
#
#
# for t in (T):
#     k1=dyn_pendule(XRK2, u)
#     k2=dyn_pendule(XRK2+(h*k1), u)
#     XRK2=XRK2+(h/2)*(k1+k2)
#     etats_RK2.append((XRK2))
#
#
# etats_RK2=np.array(etats_RK2)[:-1] # on enléve le dernier éléments comme on il y a un arg en trop à cause du for
#
#
# plt.plot(T, etats_RK2[:, 0], '-r')
# plt.legend()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
alpha = 1
beta = 1

def dynamique_lv(X, U):
    x1_dot = (1 - alpha * X[1]) * X[0]
    x2_dot = (-1 + beta * X[0]) * X[1]
    return np.array([x1_dot, x2_dot])

X_bar = np.array([1/beta, 1/alpha])
A_lin =np.array([[0, -alpha / beta], [beta / alpha, 0]])

def dynamique_lin(X, U):
    X_dot = A_lin @ (X - X_bar)
    return X_dot


X_nl = np.array([1.3, 1.5])
X_lin = X_nl.copy()
h = 1e-3
T = np.arange(0, 100, h)

res_nl = [X_nl]
res_lin = [X_lin]
for t in T[:-1]:
    k1_nl = dynamique_lv(X_nl, 0)
    k2_nl = dynamique_lv(X_nl + h * k1_nl, 0)
    X_nl = X_nl + (k1_nl + k2_nl) * h / 2
    res_nl.append(X_nl)
    k1_lin = dynamique_lin(X_lin, 0)
    k2_lin = dynamique_lin(X_lin + h * k1_lin, 0)
    X_lin = X_lin + (k1_lin + k2_lin) * h / 2
    res_lin.append(X_lin)

res_nl = np.array(res_nl)
res_lin = np.array(res_lin)
plt.plot(T, res_nl[:, 0], label="pop 0, nl")

plt.plot(T, res_lin[:, 0], label="pop 0, lin")
plt.legend()
plt.figure()
plt.plot(T, res_nl[:, 1], label="pop 1, nl")
plt.plot(T, res_lin[:, 1], label="pop 1, lin")
plt.legend()
plt.show()

plt.figure()
plt.plot(res_nl[:,0], res_nl[:, 1], label="plan de phase, nl")
plt.plot(res_lin[:, 0], res_lin[:, 1], label="plan de phase, lin")
plt.legend()
plt.show()









