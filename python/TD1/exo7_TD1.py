typeConversion = input("Type de conversion\n"
                       " a) Degrés Celsius --> Fahrenheit\n"
                       " b) Fahrenheit --> Degrés Celsius\n"
                       "Entrez a ou b : ")

if (typeConversion == 'a'):
    tempC = input("Temp en celsius : ")
    val = int(tempC) * 1.8 + 32
elif (typeConversion == 'b'):
    tempF = input("Temp en Fahrenheit : ")
    val = (int(tempF) - 32) / 1.8

print("%.2f" % val)
