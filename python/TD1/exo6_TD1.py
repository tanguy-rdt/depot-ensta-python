Deg = int(input("Degrés: "))
Min = int(input("Minutes: "))
Sec = int(input("Secondes: "))

angleDegDec = (Deg + (Min + (Sec / 60)) / 60)
angleRad = (angleDegDec * 3.14) / 180

print("Angle en degrés décimaux:", "%.3f" % angleDegDec, "°", sep=" ")
print("Angle en radian:", "%.3f" % angleRad, "rad", sep=" ")
