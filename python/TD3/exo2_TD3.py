listeInit=[432,342,5,65,35,6,22,65,876]
listPaire=[]
listImpaire=[]

for i in range (len(listeInit)-1) :
    if (listeInit[i]%2==0) :
        listPaire.append(listeInit[i])
    else :
        listImpaire.append(listeInit[i])

print("La liste à trier :", listeInit)
print("La liste paire :", listPaire)
print("La liste impaire :", listImpaire)







