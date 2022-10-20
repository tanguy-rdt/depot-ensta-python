s = 'Quarante-deux, dit Compute-Un, avec infiniment de calme et de majesté.'

def conversionStrToInt(STR) :

    global l
    # Conversion en liste d'entiers
    l = [ord(x) for x in STR]

    # Tri de la liste
    l.sort()

    res=''
    for x in l:
        if x>64:
            res += chr(x)

    return res

print(conversionStrToInt(s))


