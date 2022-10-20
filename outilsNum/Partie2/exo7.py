import numpy as np
import matplotlib.pyplot as plt


cons = [1.03, 1.01, 1.03, 1.05, 1.03, 1.21, 1.25, 1.22, 1.24, 1.24, 1.68, 1.66, 1.69, 1.69, 1.62, 2.19,
        2.3, 2.2, 2.36, 2.12, 3.14, 3.13, 2.94, 3.25, 3.19, 3.86, 3.95, 4.09, 4.11, 4.28, 5.01, 5.01,
        4.95, 5.01, 5.17, 6.91, 6.99, 6.31, 6.14, 6.17, 8.71, 8.5, 8.96, 7.75, 8.18, 10.79, 9.68, 9.93,
        10.39, 10.44, 11.04, 11.49, 11.38, 11.44, 12.0, 13.41, 15.08, 13.69, 14.04, 15.07, 15.51, 15.43,
        15.58, 15.54, 17.46]

vitesse=np.arange(5, 125+1, 10) # 5 à 125 inclus par pas de 10

cons=np.array(cons).reshape(vitesse.size, 5) # 13 lignes 5 col

cons_moy=np.mean(cons, axis=1) #la moy en travaillant sur les lignes

P=np.polyfit(vitesse, cons_moy, 2)
poly=np.poly1d(P)


plt.plot(vitesse, cons_moy, 'ro', label='conso(vitesse)')
plt.plot(vitesse, poly(vitesse), 'tab:orange', label='polynôme d\'ajustement P(vitesse)')
plt.ylabel('consommation de carburant')
plt.xlabel('vitesse')
plt.legend()
plt.title('Consommation de carburant en fonction de la vitesse')
plt.show()

