import math

def suite_mystere(n):
    somme=0
    for i in range (1, n+1) :
        somme=somme+(1/(i**2))

    return math.sqrt(6*(somme))


N=1000

print("Résultat de la suite:", suite_mystere(N), ", la limite de Un tend vers π")

