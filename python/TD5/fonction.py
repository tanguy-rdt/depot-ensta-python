import random
import donnees


def recup_lettre() :
    donnees.lettreEnCour='0'

    while (donnees.lettreEnCour.isalpha()!=1)&(donnees.lettreEnCour.lower()!=1):
        donnees.lettreEnCour=input("Insérer une lettre: ")


def choisir_mot() :
    donnees.motComplet=random.choice(donnees.listMot)


def recup_mot_masque(motComplet, lettresPropose):
    motMasque=""
    lettreTrouve=0
    for i in range (len(motComplet)):
        for j in range (len(lettresPropose)):
            if motComplet[i]==lettresPropose[j]:
                lettreTrouve=1
                motMasque+=motComplet[i]
                break

        if lettreTrouve==1:
            lettreTrouve=0
        elif lettreTrouve==0:
            motMasque=motMasque+'*'

    return motMasque


