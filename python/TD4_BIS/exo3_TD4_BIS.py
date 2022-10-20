def nbpattes(p, v, c):
    return ((p*2)+(v*4)+(c*2))


nbVaches=int(input("Nombre de vaches: "))
nbPoulets=int(input("Nombre de poulets: "))
nbCanard=int(input("Nombre de canard: "))

print("Il y a", nbpattes(nbPoulets, nbVaches, nbCanard), "pattes dans la ferme")