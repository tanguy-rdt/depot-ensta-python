import numpy as np
import matplotlib.pyplot as plt

def calculZ(vx, vy):
    return np.cos(vx)+np.sin(vy)

x = np.arange(-np.pi, np.pi, 0.1)
y = np.arange((-np.pi)/2, 3*(np.pi)/2, 0.1)
[xx, yy] = np.meshgrid(x, y)

Z=calculZ(xx, yy)
extent = np.min(x), np.max(x), np.min(y), np.max(y) #permet de donner l'étendu (l'échelle)
plt.imshow(Z, extent=extent)
plt.colorbar(label='valeur de Z')
CS=plt.contour(xx, yy, Z, colors='black')
plt.clabel(CS)
plt.title('z = cos(x) + sin(y)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

