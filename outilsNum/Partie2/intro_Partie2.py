import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 10, 100) # 100 points entre 0 et 10
plt.plot(X, np.sin(X))
plt.show()