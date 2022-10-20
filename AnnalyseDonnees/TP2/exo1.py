import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv', sep=',')

sepallength = df["sepallength"].values
sepalwidth = df["sepalwidth"].values
petallength = df["petallength"].values
petalwidth = df["petalwidth"].values
species = df["class"].values
speciesname = np.unique(species)
variablename = df.keys().values[0:-1]


# question 1
plt.scatter(petallength, petalwidth)
plt.ylabel("Largeur du pétale")
plt.xlabel("Longueur du pétale")
plt.title("Nuage de points de la longueur en fonction de la largeur du pétale")
plt.show()


# question 2
corr_coef_matrix = np.corrcoef(petallength, petalwidth)
print(corr_coef_matrix)

corr_coef = corr_coef_matrix[1][1]


# question 3
def regression_lineaire(corr_coef, x, y):
    mean_x = np.mean(x)
    var_x = np.var(x)
    e_type_x = np.sqrt(var_x)

    mean_y = np.mean(y)
    var_y = np.var(y)
    e_type_y = np.sqrt(var_y)

    a = corr_coef * (e_type_y/e_type_x)
    b = mean_y - corr_coef * ((e_type_y/e_type_x)) * mean_x

    return a, b


a, b = regression_lineaire(corr_coef, petallength, petalwidth)

fit = np.polyfit(petallength, petalwidth, 1)
poly = petallength*fit[0]+fit[1]

plt.plot(petallength, a*petallength+b, color='orange', label='Formule du cours')
plt.plot(petallength, poly, color='red', label='fct np.polyfit')
plt.scatter(petallength, petalwidth)
plt.ylabel("Largeur du pétale")
plt.xlabel("Longueur du pétale")
plt.title("Équation de la droite de régression linéaire")
plt.legend()
plt.show()


#question 4
# elles sont corrélé


#question 5
iris_setosa_petallength = []
iris_versicolor_petallength = []
iris_virginica_petallength = []

for i in range(len(species)):
    if species[i] == 'Iris-setosa':
        iris_setosa_petallength.append(petallength[i])
    elif species[i] == 'Iris-versicolor':
        iris_versicolor_petallength.append(petallength[i])
    elif species[i] == 'Iris-virginica':
        iris_virginica_petallength.append(petallength[i])

plt.hist(iris_setosa_petallength, edgecolor='black', alpha=0.5, label='iris_setosa')
plt.hist(iris_versicolor_petallength, edgecolor='black', alpha=0.5, label='iris_versicolor')
plt.hist(iris_virginica_petallength, edgecolor='black', alpha=0.5, label='iris_virginica')
plt.xlabel('Longueur de pétale')
plt.ylabel('Effectifs')
plt.title("Histogrammes de la longueur de pétale pour chaque espèce")
plt.legend()
plt.show()


# question 6
boxplot_petallength = [iris_setosa_petallength, iris_versicolor_petallength, iris_virginica_petallength]
plt.boxplot(boxplot_petallength, labels=['iris setosa', 'iris versicolor', 'iris virginica'])
plt.title("Boite à moustache de la longueur de pétale pour chaque espèce")
plt.show()


#question 7
n_cumul = len(species)
mean_species_petallength = [np.mean(iris_setosa_petallength), np.mean(iris_versicolor_petallength), np.mean(iris_virginica_petallength)]
mean_petallength = np.mean(petallength)
var_species_petallength = [np.var(iris_setosa_petallength), np.var(iris_versicolor_petallength), np.var(iris_virginica_petallength)]
n_species = [len(iris_setosa_petallength), len(iris_versicolor_petallength), len(iris_virginica_petallength)]

def var_inter_classe_petallength(n_cumul, n_species, mean_species, mean):
    ret = 0
    for i in range(len(speciesname)):
        ret += n_species[i] * (mean_species[i] - mean)**2

    return ret/n_cumul


def var_intra_classe_petallength(n_cumul, n_species, var_species):
    ret = 0
    for i in range(len(speciesname)):
        ret += n_species[i] * var_species[i]

    return ret / n_cumul

var_inter_classe = var_inter_classe_petallength(n_cumul, n_species, mean_species_petallength, mean_petallength)
var_intra_classe = var_intra_classe_petallength(n_cumul, n_species, var_species_petallength)
var_totale_formule = var_inter_classe + var_intra_classe
var_totale = np.var(petallength)

rapport_corr = np.sqrt(var_inter_classe/var_totale_formule)

print("Variance interclasse: ", var_inter_classe)
print("Variance intraclasse: ", var_intra_classe)
print("Variance total trouvé avec la formule: ", var_totale_formule)
print("Variance total trouvé avec numpy: ", var_totale)
print("Rapport de corrélation: ", rapport_corr)




