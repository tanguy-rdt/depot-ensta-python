nbMarche=int(input("Nombre de marche que le gardien monte: "))
hMarche=int(input("Hauteur des marches (cm): "))
nbAllerRetour=int(input("Nombre d'aller retour dans la journée: "))

hParcourue=(nbMarche*hMarche*2*nbAllerRetour*7)/100

print("Pour", nbMarche, "marches de", hMarche, "cm, il parcourt par semaine", hParcourue, "mètres", sep=" ")
