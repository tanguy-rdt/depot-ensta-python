x=0
y=1
z=0
n=0

val=267914296

print("n   |  F(n) ")
print(n, "|", z, sep="   ")

while y!=val :
    n+=1
    print(n, "|", y, sep="   ")
    z=x+y
    x=y
    y=z