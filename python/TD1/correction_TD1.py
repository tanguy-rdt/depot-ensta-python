# Exercice 1
pi = 3.14
r = 3.25
h = 42.18
v = (pi * (r ** 2) * h) / 3
print("Le volume est de:", v, "mettre ici la bonne unité !")

# Exercice 2
prix_ht = 100.
taux_tva = 20 # ici au sens 20%

prix_ttc = prix_ht * (1 + taux_tva / 100)
print("Le prix ttc est de:", prix_ttc)

# Exercice 3
ville_1 = "Brest"
ville_2 = "Landerneau"
distance = 25
tirets_distance = "-" * distance
print(ville_1, tirets_distance, ville_2, sep="x")

# Exercice 4
nb_marches = 100
hauteur_marches_cm = 18.69 # en cm
denivele_cm = nb_marches * hauteur_marches_cm * 5 * 7 * 2 # 5 jours, 7j/semaine, *2 pour A/R
print("Pour", nb_marches, "marches de", hauteur_marches_cm, "cm il parcourt par semaine",
                                                            denivele_cm / 100, "mètres")

# Exercice 5
nb_secs = 4592313546
# nb de secondes dans une journée
nspj = 3600 * 24
# par année (365j)
nspa = nspj * 365
# par mois (30 j)
nspm = nspj * 30

# nombre d'années dans nb_secs
nb_annees = nb_secs // nspa
reste_secs = nb_secs % nspa
nb_mois = reste_secs // nspm
reste_secs = reste_secs % nspm
nb_jours = reste_secs // nspj
reste_secs = reste_secs % nspj

print(nb_annees, nb_mois, nb_jours, reste_secs)


