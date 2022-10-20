t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre', 'Novembre','Décembre']
t3=[]


for i in range (len(t2)):
    t3.append(t2[i])
    t3.append(t1[i])

print(t3)
