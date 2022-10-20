import numpy as np
import matplotlib.pyplot as plt

#A = np.linspace(0, 4*np.pi, 120000) # à la fin le nbr d'échantillon
A = np.arange(0, 4*np.pi, 1.e-4) # équivalent à la première à la fin le pas, tab de 0 à 4pi avec pas de 1.e-4
plt.plot(A, np.sin(A), 'r-', label="sin(t)")
plt.plot(A, np.cos(A), 'tab:orange', label="cos(t)")
plt.xlabel("temps")
plt.ylabel("Amplitude")
plt.legend()
plt.show()