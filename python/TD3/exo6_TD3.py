listeNbr=[]
listeNbrPremier=[]
ind=0

for i in range (1000):
    listeNbr.append(1)

listeNbr[0]=0

#while (ind)<1000 :
#    while listeNbr[ind]!=1 :
#        ind=ind+1

#    print(ind)

#    ind=ind+1

#    for i in range (ind, 1000):
#        if i%ind==0 :
#            listeNbr[i]=0

#for i in range (1000):
#    if listeNbr[i]==1:
#        listeNbrPremier.append(i+1)

for i in range (1000) :
    if ((i%2==0)&(i!=2)) | ((i%3==0)&(i!=3)) | ((i%5==0)&(i!=5)) | ((i%7==0)&(i!=7)) | \
        ((i%11==0)&(i!=11)) | ((i%13==0)&(i!=13)) | ((i%17==0)&(i!=17)) | ((i%19==0)&(i!=19)) | \
        ((i%23==0)&(i!=23)) | ((i%29==0)&(i!=29)) | ((i%31==0)&(i!=31)):
        listeNbr[i-1]=0


for i in range (1000) :
    if (listeNbr[i]==1) :
        listeNbrPremier.append(i+1)


print(listeNbr)
print(listeNbrPremier)




