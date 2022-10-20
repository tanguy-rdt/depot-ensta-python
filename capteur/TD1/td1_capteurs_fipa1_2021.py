# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

## Lecture des données
nom_fich = "td1_pressure_measurements.txt"
mesures = np.loadtxt(nom_fich)
minMesure=np.min(mesures)
maxMesure=np.max(mesures)

# question 1
print (mesures)
print("\n\nLa valeur min:", minMesure, " mA, la valeur max:", maxMesure, "mA", end="\n")
print("Donc étendu de mesure: 0 à 40 PSI\n")

# question 2
print("PE=40 psi\n\n")

# question 3
pressions = np.arange(0, 40+5, 5)
print(pressions)

mesures_moy=mesures.mean(axis=0)
print(mesures_moy)

plt.plot(pressions, mesures_moy, '-ro')
plt.xlabel("Mesurande en PSI")
plt.ylabel("Moyenne des mesures en mA")
plt.show()

# question 4 : Sensibilités
#utiliser les valeurs moyennes autour de la valeur pour laquelle on souhaite
#estimer la sensibilité

S_5=(mesures_moy[2]-mesures_moy[0])/(10-0)
S_20=(mesures_moy[5]-mesures_moy[3])/(25-15)
S_35=(mesures_moy[8]-mesures_moy[6])/(40-30)

print ("sensibilité à 5 PSI : %.2f"%(S_5), end="\n")
print ("sensibilité à 20 PSI : %.2f"%(S_20), end="\n")
print ("sensibilité à 35 PSI : %.2f"%(S_35), end="\n\n")

#Sensibilté constante l'écart est inférieurs à 4%, capteur supposé LINEAIRE,
#sur l'étendu de mesure



# question 5
#Caractéristiques de la réponse théorique données par le constructeur
#passant par les points terminaux
pente_constructeur = (20-4)/(40)
ordonnee_origine_constructeur = 4
courbe_constructeur = pente_constructeur*pressions+ordonnee_origine_constructeur


plt.plot(pressions, courbe_constructeur, 'c-o', label="Courbe théorique")
plt.plot(pressions, mesures_moy, "r+", label="Moyenne des mesures")
plt.legend()
plt.title ("Courbe Théorique")
plt.xlabel ("Pression (PSI)")
plt.ylabel ("Courant (mA)")
plt.show()


# question 6
#la fidélité pour chaque colonne du tableau de mesure (donc pour chaque
#valeur de mesurande) 

erreur_fidel_mA = np.std(mesures, 0, ddof=1)
erreur_fidel_PSI = erreur_fidel_mA/pente_constructeur

erreur_fidel_max_mA = np.max(erreur_fidel_mA)
erreur_fidel_max_PSI = np.max(erreur_fidel_PSI)
print("L'erreur de fidélité est %5.2f mA ou %5.2f PSI"%(erreur_fidel_max_mA,erreur_fidel_max_PSI))


plt.plot(pressions, erreur_fidel_PSI, '-o')
plt.xlabel("Pression (PSI)")
plt.ylabel("Erreur de fidélité (PSI)")
plt.title("Erreur de fidélité en fonction de la pression")
plt.show()


# question 7
P, ordonnee=np.polyfit(pressions, mesures_moy, 1)
courbe_estimee =P*pressions+ordonnee

plt.plot(pressions, courbe_estimee, '-ro')
plt.xlabel("pression en PSI")
plt.ylabel("courrant en mA")
plt.title("Courbe estimé")
plt.show()

erreur_lin_mA = np.abs(courbe_estimee-mesures_moy)
erreur_lin_PSI = erreur_lin_mA/pente_constructeur

erreur_lin_max_mA = np.max(erreur_lin_mA)
erreur_lin_max_PSI = np.max(erreur_lin_PSI)
print("L'erreur de linéarité est %5.2f mA ou %5.2f PSI"%(erreur_lin_max_mA,erreur_lin_max_PSI))

plt.plot(pressions, erreur_lin_PSI)
plt.xlabel("Pression (PSI)")
plt.ylabel("Erreur de linéarité (PSI)")
plt.title("Erreur de linéarité en fonction de la pression")
plt.show()


# question 8

nbits = 8
resol_mA = (20-4)/((2**nbits)-1) # --> q=(Imax-Imin)/((2**N)-1)

erreur_resol_mA = resol_mA/2  # --> erreur_resol=q/2
erreur_resol_PSI = erreur_resol_mA/pente_constructeur
print("L'erreur de résolution est %5.2f mA ou %5.2f PSI"%(erreur_resol_mA,erreur_resol_PSI))

# question 9
erreur_just_mA = np.sqrt((erreur_resol_mA**2)+(erreur_lin_max_mA**2))
erreur_just_PSI = erreur_just_mA/pente_constructeur #np.sqrt((erreur_resol_PSI**2)+(erreur_lin_max_PSI**2))

print("L'erreur de justesse est %5.2f mA ou %5.2f PSI"%(erreur_just_mA,erreur_just_PSI))



# question 10

erreur_prec_mA = np.sqrt((erreur_just_mA**2)+(erreur_fidel_max_mA**2))
erreur_prec_PSI = erreur_prec_mA/pente_constructeur

print("L'erreur de précision est %5.2f mA ou %5.2f PSI"%(erreur_prec_mA,erreur_prec_PSI))


# question 11

class_psi = erreur_prec_PSI/40*100
print("La classe de précision %d"%(round(class_psi)))

# question 12
#Garder les vecteurs jusqu'au dernier calcul et choisir la
#valeur maximale à la toute fin -méthode vectorielle

v_erreur_just_PSI = np.sqrt((erreur_resol_PSI**2)+(erreur_lin_PSI**2))
v_erreur_fidel_PSI = erreur_fidel_PSI
v_erreur_prec_PSI = np.sqrt((v_erreur_just_PSI**2)+(v_erreur_fidel_PSI**2))

plt.figure(5)
plt.plot (pressions, v_erreur_just_PSI, 'b',label='justesse')
plt.plot (pressions, v_erreur_fidel_PSI, 'c',label='fidélité')
plt.plot (pressions, v_erreur_prec_PSI, 'r',label='précision')
plt.title ("Graphique des erreurs")
plt.xlabel ("Pression (PSI)")
plt.ylabel ("Erreur (PSI)")
plt.legend(loc='lower left')

print ("précision :")
print (v_erreur_prec_PSI)

erreur_prec_PSI_new = np.max(v_erreur_prec_PSI)
print ("précision ancienne méthode = %.2f PSI"%(erreur_prec_PSI))
print ("précision nouvelle méthode = %.2f PSI"%(erreur_prec_PSI_new))

plt.show ()