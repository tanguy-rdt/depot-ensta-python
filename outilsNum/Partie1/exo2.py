import numpy as np

foo = np.random.randint(0, 10, (np.random.randint(50, 60), np.random.randint(42, 69)))
#tableau 2D avec des valeurs allant de 0 à 9, le nombre de est entre 50 et 59, le nombre de ligne entre 42 et 68

print(foo)
print("\nLigne:", foo.shape[0], "Colonne:", foo.shape[1])
print("Le nomnbre d'éléments:", foo.size)
print("Type de donnée:", foo.dtype)

foo_float=foo.astype(float)
print("\n\n", foo_float)
print("Type de donnée:", foo_float.dtype)

print("\n\nValeur supérieur à 8 dans foo:\n", foo>8) # retourne une matrice bool, si les valeurs sont supérieur à 8, si oui True sinon False

foo_inf5=foo<5
print("\n\nMatrice inf à 5",foo_inf5)
coord_inf5=np.argwhere(foo_inf5==True)
print("\nCoord des valeurs inf à 5:\n", coord_inf5)

foo_prod2=np.where(foo_inf5==True, foo, foo*2 )
print("\nfoo *2 si val[x][y] est inf à 5:\n", foo_prod2)

bar = foo[:, 0:13:2] # toutes les lignes, col 0 à 12 avec un pas de 2
print("\n\nbar:\n", bar)
bar_copy = bar.copy() #une copie de bar
print("\n\nbar_copy:\n", bar_copy)
bar_float = bar.astype(float) #on change le type de donnée de bar
print("\n\nbar_float:\n", bar_float)
baz = foo[4:14, (1,6,11,26)] #baz = les lignes 4 à 13 et les col 1, 6, 11, 26 de foo
print("\n\nbaz:\n", baz)

foo[5, 6]=42
print(foo)

