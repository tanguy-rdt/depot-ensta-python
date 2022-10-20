import numpy as np
import matplotlib.pyplot as plt


#question 1
lux=np.linspace(50,1000,20) # mesurande de 50 à 1000 lux par pas de 50 lux
imes=0.001 # 1 mA

#tension_mesurees = vmes
vmes = np.asarray([2.14, 1.03, 0.675, 0.499, 0.395, 0.326, 0.277, 0.241, 0.213, 0.191, 0.172, 0.157, 0.145, 0.134, 0.124, 0.116, 0.109, 0.103, 0.0971, 0.0920])

#question 2
rmes=vmes/imes

plt.figure(0)
plt.plot(lux, rmes)


#question 3
sens100=(rmes[2]-rmes[0])/(lux[2]-lux[0]) # coef directeur VarS/VarE
print("sensibilité à %f lux = %f ohm/lx"%(lux[1], sens100))

sens900=(rmes[18]-rmes[16])/(lux[18]-lux[16])
print("sensibilité à %f lux = %f ohm/lx"%(lux[17], sens900))


# question 4 : R =R0 * E^(-gamma) soit rmes = R0 * lux**(-gamma)
# Estimation de R0 et gamma avec la fonction np.log
lnr = np.log(rmes)
lnlux = np.log(lux)

gamma_1, R0_1= np.polyfit(lnlux, lnr, 1)

R0 = np.exp(R0_1);
gamma = np.abs(gamma_1)
print ("R0 = %f, gamma = %f" %(R0, gamma))

plt.figure(1)
plt.plot(lux, R0*lux**(-gamma), 'r')
plt.title("Courbe Caractéristique du Capteur")
plt.xlabel ("Eclairement (lx)")
plt.ylabel ("Résistance (Ohm")

imin =np.min(np.where(lux>=400.0))
imax=np.min(np.where(lux>=600.0))
print (imin, imax, lux[imin:imax+1])
wlux = lux[imin:imax+1]
print (wlux)
wrmes = rmes[imin:imax+1]

# meilleur estimée au sens des moindres carrés
alin, blin = np.polyfit(wlux, wrmes, 1)
print("Pente=%.2f Ohm/lx, Ordonnée à l'origine=%.2f Ohm"%(np.round(alin, 2), np.round(blin, 2)))


rlin=alin*wlux+blin
plt.figure(2)
plt.plot(wlux, wrmes)
plt.plot(wlux, rlin, 'r')
plt.title("Linéarisation du capteur")
plt.xlabel("Eclairement (lx)")
plt.ylabel ("Résistance (ohm)")

#question 6
elin = np.max(np.abs(rlin-wrmes))
print ("erreur de linéarité maximum sur la plage [400, 600] lx = %5.2f ohm"%(elin))

Rc500=R0*(500)**(-gamma)
elinRelative=(elin/Rc500)*100
print ("méthode 2: erreur de linéarité maximum relative sur la plage [400, 600] lx = %4.1f %%" %(elinRelative))


#question 8
ResBruitees=[206,202,206,218,201,204,214,207,203,208]

#question 9
efid=np.std(ResBruitees, ddof=1)
print("erreur de fidélité=%5.2f ohm" %efid)
ejust=np.mean(ResBruitees)-Rc500
print("erreur de justesse= %5.2f ohm" %ejust)
eprec=np.sqrt(efid**2+ejust**2)
print("erreur de précision= %5.2f ohm" %eprec)

# hypothèse linéarité - pente droite estimée
efidlux=efid/np.abs(alin)
print("erreur de fidélité = %5.2f lux" %efidlux)
ejustlux=ejust/np.abs(alin)
print("erreur de justesse = %5.2f lux" %ejustlux)
epreclux=eprec/np.abs(alin)  #= np.sqrt(efidlux**2+ejustlux**2)
print("erreur de précision= %5.2f lux" %epreclux)


#question 10
ia=1e-3
Rc400=R0*(400)**(-gamma)
Rc600=R0*(600)**(-gamma)
Vm400=Rc400*ia
Vm600=Rc600*ia

print ("la résitance Rc400 = %7.2f ohm" %Rc400)
print ("la résitance Rc600 = %7.2f ohm" %Rc600)
print ("la tension Vm400 = %6.3f V" %Vm400)
print ("la tension Vm600 = %6.3f V" %Vm600)






plt.show()
