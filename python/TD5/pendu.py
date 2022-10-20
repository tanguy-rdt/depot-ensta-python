import fonction
import donnees

newLettre=2 #0 --> false, 1 --> true, 2 --> default
newLettreTrouver=False
etatPartie=''

while (etatPartie != 'c') & (etatPartie != 'q') :
    etatPartie=input("Faites votre choix: <c>ommencer ou <q>uitter: ")

while etatPartie!='q':
    donnees.initData()
    fonction.choisir_mot()
    print("\n", fonction.recup_mot_masque(donnees.motComplet, donnees.lettrePropose), sep="")
    #print("le mot à trouver: ", donnees.motComplet, "\n")
    print("------------------------------------------------------\n")

    while (etatPartie!='p')&(etatPartie!='g'):
        fonction.recup_lettre()

        if (len(donnees.lettreEnCour)>=2):
            print("Insérez uniquement un caractère !\n")
            newLettre=2;
        elif (len(donnees.lettrePropose)==0) :
            newLettre=1
        elif (len(donnees.lettrePropose)>0):
            for i in range(len(donnees.lettrePropose)):
                if donnees.lettreEnCour == donnees.lettrePropose[i]:
                    newLettre = 0
                elif (newLettre!=0):
                    newLettre = 1

        if (newLettre == 0):
            newLettre=0
            print("Vous avez déjà choisi cette lettre.\n")
        elif (newLettre == 1):
            donnees.lettrePropose.append(donnees.lettreEnCour)

            for i in range(len(donnees.motComplet)):
                if donnees.motComplet[i] == donnees.lettreEnCour:
                    newLettreTrouver=True
                    break
                else :
                    newLettreTrouver=False

            if newLettreTrouver==True:
                print("Bien Joué !")
            elif newLettreTrouver==False:
                donnees.nbVie=donnees.nbVie-1
                print("... non, cette lettre ne se trouve pas dans le mot...")

            donnees.motMasque = fonction.recup_mot_masque(donnees.motComplet, donnees.lettrePropose)
            print(donnees.motMasque, "\n")

            for i in range(len(donnees.motMasque)):
                if donnees.motMasque[i] == '*':
                    donnees.motTrouver = False
                    break
                else:
                    donnees.motTrouver = True

            if donnees.motTrouver == True:
                etatPartie = 'g'
                print("Félicitations ! Vous avez trouvé le mot\n\n")
                print("PENDU !!! Vous avez perdu.\n", "Le mot était: ", donnees.motComplet, "\n\n", sep="")
                print("======================================================\n")
            elif (donnees.motTrouver == False) & (donnees.nbVie == 0):
                etatPartie = 'p'
                print("PENDU !!! Vous avez perdu.\n", "Le mot était: ", donnees.motComplet, "\n\n", sep="")
                print("======================================================\n")
            else :
                print("------------------------------------------------------\n")

        newLettre=2

    while (etatPartie != 'r') & (etatPartie != 'q'):
        etatPartie = input("Faites votre choix: <r>ecommencer ou <q>uitter: ")











