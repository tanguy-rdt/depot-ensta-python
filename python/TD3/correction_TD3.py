j=0
while j<15:
    for i in range(5):
        print(i," Le soleil brille ",j)
    j+=1
# bad code avec boucle infinie ... à cause de i
i=0
while i<15:
    for i in range(5):
        print(i," Le soleil brille  ")
    i+=1



