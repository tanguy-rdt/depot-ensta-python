var=input("Entrez une chaîne de caractère: ")

nbY=0

for i in range (len(var)):
    if var[i]=='y':
        nbY+=1

if nbY!=0 :
    print("Il y a", nbY, "\'y\'", sep=" ")
else:
    print("Il n'y a pas de \'y\'")



