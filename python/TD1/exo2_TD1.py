HT=int(input("Entrez le prix HT: "))
TVA=int(input("Entrez la TVA en %: "))

TTC=((100+TVA)*HT)/100

print("Prix TTC du produit: ", TTC)