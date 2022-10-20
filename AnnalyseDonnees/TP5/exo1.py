import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# excercice 1
# question 1
# xi satellite
# ni obs
obs = np.array([6, 15, 9, 25, 17, 10, 8, 7, 3])
sat = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

nObs = 0
nSat = 0
for i in range(len(obs)):
    nObs += obs[i]
    nSat += sat[i]

num_mean = 0
for i in range(len(obs)):
    num_mean += obs[i]*sat[i]
mean = num_mean / nObs

num_var = 0
for i in range(len(obs)):
    num_var += (sat[i]-mean)**2
var = num_var/(len(sat)-1)

print("Question 1:")
print(" Moyenne =", mean)
print(' Variance =', var, end="\n\n")


#question 2
Lambda = 4.47
poisson_array = np.zeros((17,))
effectifs_th = np.zeros((17,))
print("Question 2:")
print("nb Sat |  nb Obs  |  Proba  |   eff th")
print("=========================================")
poisson_array[0] = stats.poisson.pmf(0, Lambda)
effectifs_th[0] = nObs * poisson_array[0]
print("  ", 0, "  |  ", "N.C", "  |\t", round(poisson_array[0], 3), "\t|\t", round(effectifs_th[0], 3))
print("-----------------------------------------")

for i in range(1, len(sat)+1):
    poisson_array[i] = stats.poisson.pmf(sat[i-1], Lambda)
    effectifs_th[i] = nObs * poisson_array[i]

    print("  ", sat[i-1], "  |   ", round(obs[i-1], 2), "\t |\t", round(poisson_array[i], 3), "\t|\t", round(effectifs_th[i], 3))

print("-----------------------------------------")

plt.plot(sat, poisson_array[:9], 'ro')
plt.show()

for i in range(10, 17):
    poisson_array[i] = stats.poisson.pmf(i, Lambda)
    effectifs_th[i] = nObs * poisson_array[i]

    print(" ", i, "  |  ", "N.C", "  |\t", round(poisson_array[i], 3), "\t|\t", round(effectifs_th[i], 3))

print("\n\n")

nSat16 = np.arange(0, 17, 1)
plt.plot(nSat16, poisson_array, 'ro')
plt.show()


#question 3
#1. Paramètre d’intérêt : La distribution du nombre de satellites visibles par rapport aux nombre de point d'observation
#2. Hypothèse nulle H0 : La distribution du nombre de satellites par rapport aux nombre de point d'observation  a été produit par cette loi de
#   Poisson
#3. Hypothèse alternative H1 : La distribution du nombre de satellites par rapport aux nombre de point d'observation
#   n'a pas été produit par cette loi de Poisson
#4. Tests statistique: page 201
#5. Niveau de confiance: 95%
#6. Rejet de H0 si ki2Obs > ki2,alpha,n-p-1 ou si p-valeur < 0.05

# On add les effectifs où npi < 5
i = 0
while (effectifs_th[i] < 5):
    effectifs_th[i+1] += effectifs_th[i]
    effectifs_th[i] = 0
    i += 1

i = len(effectifs_th)-1
while (effectifs_th[i] < 5):
    effectifs_th[i-1] += effectifs_th[i]
    effectifs_th[i] = 0
    i -= 1

effectifs_th = np.delete(effectifs_th, np.where(effectifs_th == 0))


k = len(effectifs_th)
p = 3 # la moyenne, l'effectif th et loi poisson
ic = 95
alpha = 1 - ic / 100
chi2 = stats.chi2.ppf(1-alpha, k-p-1)
chi2_Obs = 0

for i in range(k):
    chi2_Obs += ((obs[i]-effectifs_th[i])**2)/(effectifs_th[i])

p_valeur = 1 - stats.chi2.cdf(chi2_Obs, k-p-1)

print("Question 3:")
print(" Les effectifs théorique après modification dû aux n.pi<5 :", effectifs_th)
print(" Chi2:", chi2)
print(" Chi2 Obs:", chi2_Obs)
print(" p-valeur:", p_valeur)
print(" On ne peut pas rejeter H0, La distribution du nombre de satellites par rapport aux nombre de points d'observations à été produit par cette loi de poisson.", end="\n\n\n")


# On ne peut pas rejeter H0 donc La distribution du nombre de satellites par rapport aux nombre de point d'observation  a été produit par cette loi de
# Poisson

print("------------------------ EXERCICE 2 ------------------------\n\n")


# exercice 2
# question 1
nij = np.array([[3, 9, 18, 36, 29],
                [3, 3, 1, 14, 13]])

sum_ni = np.array([np.sum(nij[0, :]), np.sum(nij[1, :])])
sum_nj = np.array([np.sum(nij[:, 0]), np.sum(nij[:, 1]),
                   np.sum(nij[:, 2]), np.sum(nij[:, 3]), np.sum(nij[:, 4])])
sum_nij = int(np.array([np.sum(sum_ni[:])]))

print("Nous avons les données suivantes :")
print(" nij:\n", nij)
print(" sum_ni:", sum_ni)
print(" sum_nj:", sum_nj)
print(" sum nij:", sum_nij, end="\n\n")

#1. Paramètre d’intérêt : Le comportement masculins et féminins est indépendant/dépendant
#2. Hypothèse nulle H0 : Le comportement masculins et féminins est dépendant
#3. Hypothèse alternative H1 : Le comportement masculins et féminins est indépendant
#4. Tests statistique: page 207
#5. Niveau de confiance: 95%
#6. Rejet de H0 si ki2Obs > ki2,alpha,n-p-1 ou si p-valeur < 0.05

p = 2  #2 intervalles homme/femme
q = 5  #5 valeurs dans chaques intervalles
ic = 95
alpha = 1 - ic / 100
chi2 = stats.chi2.ppf(1-alpha, ((p-1)*(q-1)))
chi2_Obs = 0

for i in range(p):
    for j in range(q):
        chi2_Obs += ((nij[i][j] - ((sum_ni[i]*sum_nj[j])/(sum_nij)))**2)/((sum_ni[i]*sum_nj[j])/(sum_nij))

p_valeur = 1 - stats.chi2.cdf(chi2_Obs, ((p-1)*(q-1)))

print("Question 4:")
print(" Chi2:", chi2)
print(" Chi2 Obs:", chi2_Obs)
print(" p-valeur:", p_valeur)
print(" On ne peut pas rejeter H0, le comportement masculins et féminins est dépendant", end="\n\n\n")