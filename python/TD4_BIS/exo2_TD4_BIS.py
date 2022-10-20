a=int(input("Entrez un nombre: "))

def puissance(x):
    return x**2, x**3, x**4, x**5

print("Les 4 première puissance de", a, "sont:", puissance(a)[0], ",", puissance(a)[1], ",", puissance(a)[2], ",",
      puissance(a)[3])
