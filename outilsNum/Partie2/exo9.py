import numpy as np
import matplotlib.pyplot as plt

def coefTrans (Beta, epsilon):
    return (1)/(np.sqrt(((1-Beta**2)**2)+4*(epsilon**2)*(Beta**2)))


Beta=np.arange(0, 3, 0.01)
plt.xlim(0, 2.9)
plt.ylim(0, 8)

epsilon=[0, 0.1, 0.2]
for i in epsilon :
    plt.plot(Beta, coefTrans(Beta, i), label=i)

plt.annotate('Réponse statique sous l''effort F0', xy=(0, 1), xytext=(0.25, 2),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))


plt.legend(title='Valeur de $\epsilon$')
plt.xlabel(r'$\frac{\omega}{\omega0}$')
plt.ylabel('Facteur d''amplification dynamique')
plt.title('Atténuation vibratoire par suspensions élastiques')
plt.show()

