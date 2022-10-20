import numpy as np
import matplotlib.pyplot as plt

A = np.array([5, 2, 2, 4]).reshape(2, 2)
B = np.array([4, -2])
c = 3

def f(X):
    return np.transpose(X)@A@X + np.transpose(B)@X + c

def fp(X):
    return 2*np.transpose(X)@A + np.transpose(B)

X_min = -0.5 * np.linalg.inv(A)@B
X = np.linspace(-2, 1, 101)
Y = np.linspace(-1, 2, 151)
Z = np.zeros((X.shape[0], Y.shape[0]))

for i in range (X.shape[0]):
    for j in range (Y.shape[0]):
        point = np.array((X[i], Y[j]))
        Z[i, j] = f(point)

print("X min:", X_min)


Xg = np.array([-1.5, 1.5])
Xg_new = Xg - 0.042 * fp(Xg)

while (np.linalg.norm(Xg-Xg_new) > 1e-3):
    Xg = Xg_new
    Xg_new = Xg - 0.042 * fp(Xg)
    print(Xg_new)

#for _ in range (42):
#   Xg = Xg - 0.042 * fp(Xg)


extent = [np.min(X), np.max(X), np.min(Y), np.max(Y)] #permet de donner l'étendu (l'échelle)
plt.imshow(Z, extent=extent)
plt.colorbar(label='valeur de Z')
CS=plt.contour(Z, extent=extent, colors='black')
plt.plot(X_min[0], X_min[1], 'o')
plt.clabel(CS)
plt.show()




