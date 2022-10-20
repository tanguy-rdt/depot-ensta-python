alpha=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
       'v', 'w', 'x', 'y', 'z')
dico = {}
nbDico = 0
Cesar = 2
motTemp=[]

def creatDico(STR):
    global nbDico
    motTemp = []

    for i in range (len(mot)) :
        motTemp.append(mot[i])

    dico[nbDico]=motTemp
    print("Mot non chiffré: ", dico[nbDico])
    nbDico=nbDico+1


def chiffrement(NBDico, ALPHA):
    for i in range (len(dico[NBDico])):
        for j in range (len(ALPHA)):
            if (dico[NBDico][i]==ALPHA[j])&(j==24):
                dico[NBDico][i] = ALPHA[0]
                break
            elif (dico[NBDico][i]==ALPHA[j])&(j==25):
                dico[NBDico][i] = ALPHA[1]
                break
            elif dico[NBDico][i]==ALPHA[j] :
                dico[NBDico][i]=ALPHA[j+Cesar]
                break

    print("Mot chiffré: ", dico[NBDico])


def dechiffrement (NBDico, ALPHA):
    for i in range (len(dico[NBDico])):
        for j in range (len(ALPHA)):
            if (dico[NBDico][i]==ALPHA[j])&(j==0):
                dico[NBDico][i] = ALPHA[24]
                break
            elif (dico[NBDico][i]==ALPHA[j])&(j==1):
                dico[NBDico][i] = ALPHA[25]
                break
            elif dico[NBDico][i]==ALPHA[j] :
                dico[NBDico][i]=ALPHA[j-Cesar]
                break

    print("Mot déchiffré: ", dico[NBDico])

commande=input("<c> Pour chiffrer, <v> pour consulter et <t> pour terminer: ")

while commande != 't' :

    if commande == 'c' :
        mot = input("Mot à chiffrer: ")
        creatDico(mot)
        chiffrement(nbDico-1, alpha)
    elif commande == 'v' :
        posMot=int(input("Pos du mot à déchiffrer: "))
        print("Mot chiffré: ", dico[posMot])
        dechiffrement(posMot, alpha)

    commande = input("<c> Pour chiffrer, <v> pour consulter et <t> pour terminer: ")


