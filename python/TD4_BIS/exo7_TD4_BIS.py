def somme_carres(n):
    Somme = 0
    listSomme=[]
    for i in range (n+1):
        Somme = Somme+(i**2)
        listSomme.append(Somme)

    return Somme, listSomme


n=int(input("Entrez un entier: "))

print("Somme des carrés de tous les entiers de 0 à", n, "est de:", somme_carres(n)[0])
print(somme_carres(n)[1])
