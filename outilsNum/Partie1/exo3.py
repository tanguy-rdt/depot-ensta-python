import numpy as np

short_sides = np.random.randint(1, 10, (200,2))

hypo=np.sqrt((short_sides[:, 0]**2) + (short_sides[:, 1]**2))
#hypot=np.hypot(short_sides[:, 0], short_sides[:, 1])

triangle=np.column_stack((short_sides, hypo)) # (()) pour faire un tuple
angle=np.array([np.degrees(np.arccos((triangle[:, 0])/(triangle[:, 2]))), np.degrees(np.arccos((triangle[:, 1])/(triangle[:, 2])))])
equal=np.allclose(angle[0, :], angle [1, :], 13)




# tab[2::3, ::2]
#   Toutes les lignes à partir de la 2ème par pas de 3 et toutes les colonnes par pas de 2
#
# Les valeurs trouvées sont elle toutes égales ? Pourquoi ?
# Non, les longueurs des côtés sont aléatoires, certain angle sont égaux
#
# Peut-on tout de même savoir si les valeurs trouvées sont toutes à peu près égales ?
#   Oui avec allclose
#
# Quel est le sens de "à peu près" dans la fonction que vous venez d'utiliser pour la question précédente
#   les valeurs sont à peu près égales avec une tolérence de 13 degrès

