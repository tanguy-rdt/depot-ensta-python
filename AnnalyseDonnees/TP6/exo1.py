import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# question 1
# Proportion de carbonne --> qualitative
# Résistance à la traction  --> quantitative

# question 2
p = 4
n = 7

resistance_01 = [23.05, 36, 31.1, 32.65, 30.9, 31.4, 30.85]
resistance_02 = [41.85, 25.65, 46.7, 34.5, 36.65, 31.45, 36.13]
resistance_04 = [47.05, 43.45, 43, 38.65, 41.85, 35.45, 41.57]
resistance_06 = [49.65, 73.9, 66.45, 74.55, 62.4, 63.75, 65.11]
p_carbonne    = [0.1, 0.2, 0.4, 0.6]

resistance = [resistance_01, resistance_02, resistance_04, resistance_06]

resistance_classe_mean = []
for i in range(p):
    sum = 0
    for j in range(n):
        sum += resistance[i][j]
    resistance_classe_mean.append(sum/n)

resistance_classe_var = []
for i in range(p):
    sum = 0
    for j in range(n):
        sum += (resistance[i][j] - resistance_classe_mean[i])**2
    resistance_classe_var.append(sum/(n-1))


print("Question 2:")
for i in range(p):
    print("\t--> ", p_carbonne[i], "% de carbonne: moy =", resistance_classe_mean[i], " et var =", resistance_classe_var[i])
print("\n")

plt.boxplot(resistance, labels=['Carbonne 0.1%', 'Carbonne 0.2%', 'Carbonne 0.4%', 'Carbonne 0.6%'])
plt.title("Boite à moustache de la résistance à la traction de \nsept éprouvettes pour différent acier")
plt.show()



# question 3


N = p * n
resistance_global_mean = 0
for i in range(p):
    for j in range(n):
        resistance_global_mean += resistance[i][j]
resistance_global_mean /= N


disp_intraclasse_tot = 0
for i in range(p):
    disp_intraclasse_tot += (n*resistance_classe_var[i])
disp_intraclasse_tot /= N


disp_interclasse = 0
for i in range(p):
    disp_interclasse += n*(resistance_classe_mean[i]-resistance_global_mean)**2
disp_interclasse /= N


#1. Paramètre d’intérêt : proportion de carbone
#2. Hypothèse nulle H0 : La proportion de carbone n'a pas d'influence sur la résistance à la traction
#3. Hypothèse alternative H1 : La proportion de carbone a une influence sur la résistance à la traction
#4. Tests statistique: test de fisher
#5. Niveau de confiance: 95%
#6. Rejet de H0 si f0 > f ou si p-valeur < 0.05

ic = 95
alpha = 1 - (ic/100)
f = stats.f.ppf(1-alpha, (p-1), (N-p))
f0 = ((disp_interclasse)/(p-1))/((disp_intraclasse_tot)/(N-p))
p_valeur = 1 - stats.f.cdf(f0, (p-1), (N-p))

print("Question 3:")
print("\t--> Moyenne global=", resistance_global_mean)
print("\t--> Dispersion intraclasse totale=", disp_intraclasse_tot)
print("\t--> Dispersion interclasse=", disp_interclasse, end="\n\n")
print("\t----------- TEST -----------\n")
print("\t--> f=", f)
print("\t--> f0=", f0)
print("\t--> p-valeur=", p_valeur)









