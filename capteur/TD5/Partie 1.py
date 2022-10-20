import numpy as np
import matplotlib.pyplot as plt

F = np.arange(0, 200 + 1, 2)

Ia = 10e-3
R = 10
K = 2.08
S = 10e-9
E = 1.6e11

Dlrelative = F / S / E
DR = K * R * Dlrelative
Vmes = Ia * (R * DR) / (4 * R + DR)

a, b = np.polyfit(F, Vmes, 1)
courbe_estimee = a * F + b

plt.plot(F, Vmes, '-b', label="Vmes Théorique")
plt.plot(F, courbe_estimee, '-r', label="Vmes Estimée")
plt.legend()
plt.show()

Sensi = a
erreur_lin_V = np.abs(Vmes - courbe_estimee)
erreur_lin_V_max = np.max(erreur_lin_V)
print("L'erreur de linéarité max en V est de:", erreur_lin_V_max, "V")


erreur_lin_N = np.abs(Vmes - courbe_estimee)/Sensi
erreur_lin_N_max = np.max(erreur_lin_N)
print("L'erreur de linéarité max en N est de:", erreur_lin_N_max, "N")


PE=200-0
classe=100*erreur_lin_N_max/PE
print("Classe du capteur %5.2f en pourcent de PE" %(classe))

nb_brins=10
deltaRj=(DR/R)*nb_brins*R
print("Delta Rj =", deltaRj)