# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:06:49 2015

@author: gautropa
"""


# exercice1 du TDSaison1Episode4
# Mini système de bases de données
def consultation():
    while 1:
        nom = input("Entrez le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        if nom in dico:  # le nom est-il répertorié ?
            item = dico[nom]  # consultaion proprement dite
            age, taille = item[0], item[1]
            print("Nom : {} - âge : {} ans - taille : {} m.". \
                  format(nom, age, taille))
        else:
            print("*** nom inconnu ! ***")


def remplissage():
    while 1:
        nom = input("Entrez le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        age = int(input("Entrez l'âge (nombre entier !) : "))
        taille = float(input("Entrez la taille (en mètres) : "))
        dico[nom] = (age, taille)


dico = {}
while 1:
    choix = input("Choisissez : (R)emplir - (C)onsulter - (T)erminer : ")
    if choix.upper() == 'T':
        break
    elif choix.upper() == 'R':
        remplissage()
    elif choix.upper() == 'C':
        consultation()

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:57:43 2015

@author: toumiab-gautropa
"""










# exercice2 du TDSaison1Episode4
# import string
# fabric du dictionnaire pour le mot
def fabricdico(mot):
    for e in mot:
        dic_chiff[e] = chr(((ord(e) - ord('a') + cesar) % 26) + ord('a'))
        print(ord(e))  # code ascii en decimal
        print(chr(ord(e)))
        print("(ord(e) - ord('a') + cesar) % 26 ", (ord(e) - ord('a') + cesar) % 26)
        print("(ord(e) - ord('a') + cesar) % 26 + ord('a') ", (ord(e) - ord('a') + cesar) % 26 + ord('a'))
        print("chr((ord(e) - ord('a') + cesar) % 26 + ord('a')) ", chr((ord(e) - ord('a') + cesar) % 26 + ord('a')))
    print("le dico de chiff : ", dic_chiff)


def chiffrermot(mot):
    mot_chiff = ''
    for e in mot:
        mot_chiff += dic_chiff[e]
    print(" le mot chiffre in : ", mot_chiff)
    return mot_chiff


def dechiffrermot(mot_chiff):
    for (c, val) in dic_chiff.items():
        dic_dech[val] = c
    #    dic_dech = dict((val, c) for c, val in dic_chiff.items())

    print("le dico de dechiff : ", dic_dech)

    # for mot in mots_chiff:
    print("coucou ", mot)
    print("coucou ", mot_chiff)
    mot_init = ''
    for e in mot_chiff:
        mot_init += dic_dech[e]
    print("le chiffrement de '{0}' est : {1} ".format(mot_chiff, mot_init))


# programme pricipal

mot = "python"

dic_chiff = {}  # dictionnaire de chiffrement
dic_dech = {}  # dictionnaire de dechiffrement
cesar = int(input("Donner le chiffre de César (<26) :"))
if cesar < 26 and cesar > 0:
    fabricdico(mot)
    mot_chiffre = chiffrermot(mot)
    print(" le mot chiffre out : ", mot_chiffre)
    dechiffrermot(mot_chiffre)
else:
    print("Merci d'introduire un nombre <26 et >0 !")
    cesar = 1  # valeur par defaut










#Exercice 7 "Base de données nom/âge/taille"

#Initialisation du dictionnaire
dico = {}

#Choix de l'utilisateur
print("Quelle action voulez-vous faire ?")

while 1:
    choix = input("Choisissez : (R)emplir - (C)onsulter - (T)erminer :")
    if choix.upper() == "T":
        print("Terminé")
        break
    # Premier bloc : remplissage du dictionnaire
    elif choix.upper() == "R":
        print("Remplissage du dictionnaire")
        while 1:
            nom = input("Entrez le nom (ou <enter> pour terminer) :")
            if nom == "":
                break
            age = int(input("Entrez l'âge (nombre entier !) :"))
            taille = float(input("Entrez la taille (en mètres) :"))
            dico[nom] = (age, taille)
    # Deuxième bloc : consultation du dictionnaire
    elif choix.upper() == "C":
        print("Consultation du dictionnaire")
        while 1:
            recherche = input("Quel nom recherchez-vous ? (<entrer> pour terminer) ")
            if recherche == "":
                break
            if recherche not in dico:
                print("Le nom n'existe pas - Nouvel essai")
            else :
                print("Nom :{} - âge :{} ans - taille :{} m.".format(recherche, dico[recherche][0], dico[recherche][1]))
