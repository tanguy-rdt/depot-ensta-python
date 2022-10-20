listNote=[]
a=1
moy=0

while a>0 :
    a=int(input("Entrez une note :"))

    if a>0 :
        listNote.append(a)

    print("Le nombre de note est: ", len(listNote))

    listNote.sort()
    print("La note la plus haute est: ", listNote[len(listNote) - 1])
    print("La note la plus basse est: ", listNote[0])

    if (len(listNote)>1):
        for i in range(len(listNote) - 1):
            moy = moy + listNote[i]

        moy = moy / (len(listNote))

    else :
        moy = listNote[0]

    print("La moyenne est de: ", moy)
    print("\n\n")







