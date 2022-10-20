speedMph=input("Vitesse en miles/heure: ")
speedKmh=(int(speedMph)*1609)/1000
speedMs=(int(speedMph)*1609)*(1/3600)

print("vitesse en Km/h :", speedKmh, "Km/h")
print("Vitesse en m/s :", speedMs, "m/s")