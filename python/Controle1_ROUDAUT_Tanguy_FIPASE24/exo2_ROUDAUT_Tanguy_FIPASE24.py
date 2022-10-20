def syracuse(h, n):
    Un=h # initial U0=h

    for i in range (1, n+1): # on calcul Un le nombre d'itération souhaité donc n
        if Un%2==0: # si Un est paire
            Un=(Un//2)
        else : # si Un est impaire
            Un=1+3*Un

    return Un # retour de Un



def syracuse_liste(h, n):
    Un=h # initial U0=h
    liste_syracuse=[Un] # On créer la liste Un avec comme première valeur Uo

    for i in range (1, n+1): # On refait comme dans la func syracuse
        if Un%2==0:
            Un=(Un//2)
        else :
            Un=1+3*Un

        liste_syracuse.append(Un) # On ajoute à la liste la nouvelle valeur de Un

    return liste_syracuse # On retourne la liste



def temps_de_vol(h):
    Un=h
    n=0

    while (Un!=1) : #On fait tant que la valeur de Un n'est pas de 1
        if Un%2==0:
            Un=(Un//2)
        else :
            Un=1+3*Un

        n+=1 #On incrémente les itérations

    return n # On retourne le nombre d'itération quand Un=1



def temps_de_vol_MAX(hmin, hmax):
    n_max=0
    u_n_max=0
    for i in range (hmin, hmax+1) : # On parcours pour la valeur Uo min à max
        if temps_de_vol(i)>n_max : # On compare si le nouveau temps de vol est plus long que l'ancien
            n_max=temps_de_vol(i) # si Oui on change n_max par la nouvelle valeur
            u_n_max=i

    return n_max, u_n_max

h=15
n=20
hmin=1
hmax=100

# Affiche la valeur de Un en fonction de U0 et et n
print("La suite Un avec U0=", h, "et avec", n, "itération, est égale à:", syracuse(h, n), sep=" ", end="\n")

# Affiche la liste des différentes valeurs de Un
print("Les différentes valeurs de Un pour U0=", h, "avec", n, "itération sont:", syracuse_liste(h, n), sep=" ", end="\n")

# Affiche le temps de vol en fonction Uo, donc le nombres d'itérations nécessaires pour Un=1
print("Le temps de vol pour U0=", h, "est de:", temps_de_vol(h), "itérations", sep=" ", end="\n")

#Affiche le temps de vol le plus long pour U0min et U0max
print("Le temps de vol max pour U0=", hmin, "à U0=", hmax, "est de:", temps_de_vol_MAX(hmin, hmax)[0],"itérations",
      "à la valeur U0=", temps_de_vol_MAX(hmin, hmax)[1], sep=" ", end="\n")


# ****************************************************************************************************************************************
#                                                              RESULTAT exo 2
# ****************************************************************************************************************************************

#La suite Un avec U0= 15 et avec 20 itération, est égale à: 1
#Les différentes valeurs de Un pour U0= 15 avec 20 itération sont: [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1]
#Le temps de vol pour U0= 15 est de: 17 itérations
#Le temps de vol max pour U0= 1 à U0= 100 est de: 118 itérations à la valeur U0= 97