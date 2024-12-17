def vocales(oración):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in oración:
        if letra in vocales:
            contador = contador + 1
    return contador
print("Dime una oración")
oración = input()
print ("La oración tiene",(vocales(oración)),"vocales.")