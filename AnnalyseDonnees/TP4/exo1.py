import numpy as np
from scipy import stats

# question 1
# procédure
# 1. Grandeur d'intéret --> Proportion de personne de plus de 40 ans participent à du fitness
# 2. H0 --> p = p0 = 20% soit la proportion de personne de plus de 40 ans participent à du fitness et de 20%
# 3. H1 --> p < p0 = 20% soit la proportion de personne de plus de 40 ans participent à du fitness et infeérieur à 20%
# 4. Test statistique --> Statistique unilatérale grand échantillon (n = 100) avec n.(1-p0)=80 et n.p0=20 soit > 5
# 5. Niveau de confiance --> 95%
# 6. Rejet de H0 si --> z0 < -z et p-valeur < 0.05 (résultats sont statistiquement significatif)

n = 100
p0 = .2
p = 15/n
ic = 95
alpha = 1 - ic / 100
z = stats.norm.ppf(1 - alpha)
z0 = (p - p0)/np.sqrt(p0*(1-p0)/n)
p_valeur = stats.norm.cdf(z0)

print("Question 1:")
print(" z:", round(z, 3))
print(" z0:", round(z0, 3))
print(" p-valeur:", p_valeur, end="\n\n")

"""
Question 1:
 z: 1.645
 z0: -1.25
 p-valeur: 0.10564977366685518
 
 z0 < -z mais les résultats ne sont pas statistiquement significatif comme p-valeur > 0.05, donc on ne peut pas rejeter H0
"""


# question 2
# procédure
# 1. Grandeur d'intéret --> moyenne
# 2. H0 --> u = u0 = 37,5
# 3. H1 --> u différent de u0 = 37,5
# 4. Test statistique --> Statistique bilatéral pour la moyenne d'une distribution normal de var inconnue
# 5. Niveau de confiance --> 95%
# 6. Rejet de H0 ? --> page 175

x = np.array([39, 39, 40, 33, 36, 40, 37, 41, 39, 34, 42, 41, 42, 44, 42, 42, 39, 42, 41, 40, 43, 43, 40, 39, 37])
n = len(x)
u0 = 37.5
xn = np.mean(x)
ecart_type_x = np.std(x, ddof=1)
ic = 95
alpha = 1 - ic / 100
t = stats.t.ppf(1 - (alpha / 2), n - 1)
t0 = (xn - u0)/(ecart_type_x/np.sqrt(n))
p_valeur = 2 - 2 * stats.norm.cdf(np.abs(t0))

print("Question 2:")
print(" t:", round(t, 3))
print(" t0:", round(t0, 3))
print(" p-valeur:", p_valeur, end="\n\n")

"""
Question 2:
 t: 2.064
 t0: 2.064
 p-valeur: 2.678522342547396e-05
 
 t0 > t, deplus p-valeur << 0.05, les résultats sont alors hautement significatifs, nous pouvons rejeter H0 et dire que l'année 2016 est exceptionnel
"""


# question 3
# procédure
# 1. Grandeur d'intéret -->
# 2. H0 -->
# 3. H1 -->
# 4. Test statistique -->
# 5. Niveau de confiance -->
# 6. Rejet de H0 ? -->

n = 100
u0 = 80/100
xn = 79.7/100
ecart_type_x = .8/100
ic = 95
alpha = 1 - ic / 100
z = stats.norm.ppf(1 - (alpha / 2))
z0 = (xn - u0)/(ecart_type_x/np.sqrt(n))
p_valeur = 2 - 2 * stats.norm.cdf(np.abs(z0))

print("Question 3:")
print(" z:", round(z, 3))
print(" z0:", round(z0, 3))
print(" p-valeur:", p_valeur)

"""
Question 3:
 z: 1.96
 z0: -3.75
 p-valeur: 0.00017683457040162942
 
  z0 < -z et p-valeur << 0.05, les résultats sont alors hautement significatifs nous pouvons rejeter H0 et dire que 
"""


