dico={}
dico['Pierre']=(31, 1.70)

print("*****************************************************")
print("* Choisissez: (R)emplir - (C)onsulter - (T)erminer: *")
print("*****************************************************")
choix=input("")

while (choix!='T')&(choix!='t') :
        if (choix == 'R') | (choix == 'r'):
                nom = input("Entrez le nom (ou <q> pour terminer): ")

                while (nom != 'Q') & (nom != 'q'):
                        age = input("Entrez l'âge (nombre entier !): ")
                        taille = input("Entrez la taille (en mètres): ")
                        dico[nom] = (age, taille)

                        nom = input("\nEntrez le nom (ou <q> pour terminer): ")


        if (choix=='C')|(choix=='c') :
                nom = input("Entrez le nom (ou <q> pour terminer): ")

                while (nom != 'Q') & (nom != 'q'):
                        age=dico[nom][0]
                        taille=dico[nom][1]
                        print("Nom:", nom, "- âge:", age, "ans", "- taille:", taille,  "m.", sep=" ")

                        nom = input("\nEntrez le nom (ou <q> pour terminer): ")

        print("\n\n\n*****************************************************")
        print("* Choisissez: (R)emplir - (C)onsulter - (T)erminer: *")
        print("*****************************************************")
        choix = input("")




