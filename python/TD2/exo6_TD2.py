Sn=0

n=int(input("Nombre d'itérration: "))

for i in range (n):
    U=(8*((-1)**i))/(((2*i)+1)*((2*i)+3))
    Sn=Sn+U

pi=(Sn+4)/2

print("La valeur approché de pi après", n, "itérations est de:", pi, sep=" ")
