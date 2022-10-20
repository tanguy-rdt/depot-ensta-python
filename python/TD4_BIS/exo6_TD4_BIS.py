def somme_carres(n):
    return (n*(n+1)*(2*n+1))/6


n=int(input("Entrez un entier: "))

print("Somme des carrés de tous les entiers de 0 à", n, "est de:", somme_carres(n))
