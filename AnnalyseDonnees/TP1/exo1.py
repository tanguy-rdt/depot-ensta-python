import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('iris.csv', sep=',')

sepallength = df["sepallength"].values
sepalwidth = df["sepalwidth"].values
petallength = df["petallength"].values
petalwidth = df["petalwidth"].values
species = df["class"].values
speciesname = np.unique(species)
variablename = df.keys().values[0:-1]

# question 2
print("Nombre d'individus statistiques: ", len(df.values))
# il ya 150 individus statistique

# question 3
print(speciesname)
# Les variables qualitatives sont les différentes espèces des iris et leurs modalité sont  ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']
# Les variables sont nominal
# Leurs modalités sont les mesures

# question 4
print(variablename)
# Les variables quantitatives sont les différentes mesures ['sepallength' 'sepalwidth' 'petallength' 'petalwidth']
# Ce sont des variables discrètes

# question 5
iris_setosa = 0
iris_versicolor = 0
iris_virginica = 0
for i in species:
    if i == 'Iris-setosa':
        iris_setosa += 1
    elif i == 'Iris-versicolor':
        iris_versicolor += 1
    elif i == 'Iris-virginica':
        iris_virginica += 1

print("\n\n\neffectif de la modalité iris_setosa", iris_setosa)
print("effectif de la modalité iris_versicolor", iris_versicolor)
print("effectif de la modalité iris_virginica", iris_virginica)

# question 6
nb_species = np.array([iris_setosa, iris_versicolor, iris_virginica])
plt.pie(nb_species, labels=["iris setosa", "iris versicolor", "iris virginica"])
plt.title("Camenbert des variables qualitatives")
plt.show()

plt.hist(nb_species)
plt.title("Histograme des variables qualitatives")
plt.xlabel("Effectif par espèces")
plt.ylabel('Fréquence')
plt.show()

# question 7
n, x, _ = plt.hist(petallength, 50, edgecolor='black')
plt.title("Histograme en fréquence")
plt.xlabel('Longueur des pétales')
plt.ylabel('Fréquence')
plt.show()

n_cumul, _, _ = plt.hist(petallength, 50, cumulative=True, edgecolor='black')
plt.title("Histograme en fréquence cumulées")
plt.xlabel('Longueur des pétales')
plt.ylabel('Fréquence')
plt.show()


# question 9
plt.boxplot(petallength)
plt.title("Boite à moustache")
plt.show()

# question 10
def mean(n, x):
    n_max = len(df.values)
    res = 0
    for i in range(len(n)):
        res += (n[i] * x[i])
    ret = (1 / n_max) * res

    return round(ret, 3)


def median(n, x):
    n_median = (len(df.values) / 2)
    n_median_index = np.where(n == n_median)

    return float(x[n_median_index])


def variance(n, x, mean):
    n_max = len(df.values)
    res = 0
    for i in range(len(n)):
        res += n[i] * (x[i] - mean) ** 2
    ret = (1 / (n_max - 1)) * res

    return round(ret, 3)


def ecart_type(var):
    return round(np.sqrt(var), 3)


def quartiles(n, x):
    res = x[np.where(n <= len(df.values) / 4)]
    q1 = res[-1]

    res = x[np.where(n <= (3 * len(df.values)) / 4)]
    q3 = res[-1]

    q2 = median(n_cumul, x)

    return q1, q2, q3



print("\n\n\nRESUME NUMERIQUE DE LOCALISATION :")
print("Moyenne de petallenght:", mean(n, x))
print("Median de petallenght:", median(n_cumul, x))

plt.hist(petallength, 50, cumulative=True, edgecolor='black', alpha=0.5)
plt.axvline(x=mean(n, x), ymin=0, ymax=.40, color="blue", label="Moyenne", linestyle='--')
plt.axvline(x=median(n_cumul, x), ymin=0, ymax=.51, color="red", label="Median", linestyle='--')
plt.axhline(y=(len(df.values) / 2), xmin=0, xmax=.57, color="red", linestyle='--')
plt.xlabel('Longueur des pétales')
plt.ylabel('Fréquence')
plt.legend()
plt.title('Résumé numérique de localisation')
plt.show()


q1, q2, q3 = quartiles(n_cumul, x)

print("\n\n\nRESUME NUMERIQUE DE DISPERSION :")
print("Ecart-Type:", ecart_type(variance(n, x, mean(n, x))))
print("Variance:", variance(n, x, mean(n, x)))
print("Quartiles:", '\tq1 =', q1, '\tq2 =', q2, '\tq3 =', q3)

plt.hist(petallength, 50, cumulative=True, edgecolor='black', alpha=0.5)
plt.axvline(x=q1, ymin=0, ymax=.33, color="orange", label="q1", linestyle='--')
plt.axvline(x=q2, ymin=0, ymax=.51, color="red", label="q2/Median", linestyle='--')
plt.axvline(x=q3, ymin=0, ymax=.71, color="blue", label="q3", linestyle='--')
plt.xlabel('Longueur des pétales')
plt.ylabel('Fréquence')
plt.legend()
plt.title('Résumé numérique de dispersion')
plt.show()

print(min(x))
print(max(x))

plt.boxplot(petallength)
plt.axhline(y=min(x), xmax=.70, color="lightblue", label="min", linestyle='--')
plt.axhline(y=max(x), xmax=.70, color="blue", label="max", linestyle='--')
plt.axhline(y=q1, xmax=.70, color="orange", label="q1", linestyle='--')
plt.axhline(y=q2, xmax=.70, color="red", label="q2/Median", linestyle='--')
plt.axhline(y=q3, xmax=.70, color="grey", label="q3", linestyle='--')
plt.legend()
plt.title("Boite à moustache")
plt.show()