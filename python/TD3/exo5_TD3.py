list=["pierre", "paul", "jacques", "bonjour", "soleil", "nuage", "neige", "pluie", "masque", "table"]
mot=[]
motTrouve=[]
nbLettre=0
nbMot=0
motAdd=0

lettre='A'

while lettre.isupper()==1 :
    lettre=input("Entrez une lettre minuscule à trouver: ")

for i in range (len(list)):
    mot=[]
    mot[0:0]=list[i]

    print(mot)

    for j in range (len(mot)):
        if mot[j]==lettre :
            if motAdd==0 :
                motTrouve.append(list[i])
                motAdd=1
                nbMot=nbMot+1

            nbLettre=nbLettre+1

    motAdd=0

print("Nombre de lettre trouvé: ", nbLettre)
print("Nombre de mot trouvé avec la lettre: ", nbMot)
print("La liste des mots: ", motTrouve)



