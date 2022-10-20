import numpy as np
import matplotlib.pyplot as plt


def f(Zr, Zi, Cr):
    return (Zr**2) + (Zi**2) + (Cr)

def g(Zr, Zi, Ci):
    return (2*Zr*Zi)+Ci

#préliminaire
x=np.linspace(-2.1, 0.6, 100)
y=np.linspace(-1.2, 1.2, 100)
[Cr, Ci] = np.meshgrid(x, y)

Zr=np.zeros(np.shape(Cr))
Zi=np.zeros(np.shape(Ci))
res=np.zeros(np.shape(Ci))


#Algorithme
N=100
mask=np.zeros(N, dtype=bool)
res=[]

for k in range(N):
    Zr, Zi = f(Zr, Zi, Cr), g(Zr, Zi, Ci)
    mask[k]=np.all((Zr** 2 + Zi** 2) > 4)
    if (mask[k]==True):
        res.append(k)


coorfMaskTrue = np.argwhere(mask == True)
Zr[coorfMaskTrue[:, 0], coorfMaskTrue[:, 1]] = np.nan
Zi[coorfMaskTrue[:, 0], coorfMaskTrue[:, 1]] = np.nan

plt.imshow(res, cmap="turbo")
plt.show()




















