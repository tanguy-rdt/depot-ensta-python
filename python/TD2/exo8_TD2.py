var=str(input("Entrez une chaîne de caractère: "))
var=list(reversed(var))
res=""

for i in range (len(var)):
    res=res+var[i]

print("Votre chaîne de caractère inversé:", res, sep=" ")
