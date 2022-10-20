nbSecondeInit = int(input("Nombre de seconde à convertir: "))
nbSeconde = nbSecondeInit

YEAR = 365 * 24 * 3600
MONTH = 30 * 24 * 3600
DAY = 24 * 3600
HOUR = 3600
MINUTE = 60
SECONDE = 1


def calcul(typeConversion, Seconde):
    return Seconde // typeConversion, Seconde % typeConversion


nbYear = calcul(YEAR, nbSeconde)[0]
nbSeconde = calcul(YEAR, nbSeconde)[1]
nbMonth = calcul(MONTH, nbSeconde)[0]
nbSeconde = calcul(MONTH, nbSeconde)[1]
nbDay = calcul(DAY, nbSeconde)[0]
nbSeconde = calcul(DAY, nbSeconde)[1]
nbHour = calcul(HOUR, nbSeconde)[0]
nbSeconde = calcul(HOUR, nbSeconde)[1]
nbMinute = calcul(MINUTE, nbSeconde)[0]
nbSeconde = calcul(MINUTE, nbSeconde)[1]
nbSeconde = calcul(SECONDE, nbSeconde)[0]

print(nbSecondeInit, "secondes est égale à:", nbYear, "années,", nbMonth, "mois,", nbDay, "jours,", nbHour, "heurs,",
      nbMinute, "minutes", nbSeconde, "secondes", sep=" ")
