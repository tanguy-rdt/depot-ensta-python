liste_nombres = [15, 34, 89, 33, 11, 28, 18, 981, 42, 12, 69]

def moyenne(liste): # fonction qui permet de calculer et de retourner la moyenne d'une liste
    moy=0 # on init la variable moy
    for i in range (len(liste)): # on parcoure tous les éléments de la liste "liste"
        moy=moy+liste[i] # à la fin du for on obtient la somme de tous les éléments de la listes

    return moy/(len(liste)) # on retourne la moyenne, soit la somme divisé par le nombre d'éléments dans la liste

def multiple3(liste): # fonction qui retourne une liste contenant les multiples de 3 d'une autre liste
    liste_multiple3=[] # on init la liste des multiples de 3
    for i in range (len(liste)):
        if ((liste[i]%3)==0) : # si la valeur de "liste" à l'index "i" modulo 3 à un reste de 0, la valeur est un multiple de 3
            liste_multiple3.append(liste[i]) # Donc on ajoute cette valeur à la fin de la liste

    return liste_multiple3 # On retourne la liste




liste_nombres.sort() # tri la liste dans l'ordre croissant
print("Le nombre min de la liste est:", liste_nombres[0], sep=" ", end="\n") # On affiche le nombre min de la liste

print("La moyenne de la liste est de:", "%.2f"%moyenne(liste_nombres), sep=" ", end="\n") # On affiche la moy de la liste
                                        # |-> "%.2f" permet d'avoir deux chiffres après la virgule

liste_nombres_multiple3=multiple3(liste_nombres) # On créer une nouvelle liste qui contient les multiples de 3 de la liste
print("La liste des multiple de trois:", liste_nombres_multiple3, sep=" ", end="\n") # On affiche les multiples de 3 de la liste


# ****************************************************************************************************************************************
#                                                              RESULTAT exo 1
# ****************************************************************************************************************************************
# Le nombre min de la liste est: 11
# La moyenne de la liste est de: 121.09
# La liste des multiple de trois: [12, 15, 18, 33, 42, 69, 981]


