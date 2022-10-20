res=1

fact=int(input("Factoriel: "))

for i in range (1, fact):
    res=res*i

lenRes=len(str(res))

print("le nombre de chiffres dans ", fact,"! est de: ", lenRes, sep="")


