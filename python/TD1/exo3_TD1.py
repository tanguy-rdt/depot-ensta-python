from random import *

villeA=input("Entrez le nom de la ville de départ: ")
villeB=input("Entrez le nom de la ville d'arriver: ")
villeA=villeA+" x"
villeB="x "+villeB
n=randint(10, 40)


print(villeA, villeB, sep="-"*n)
