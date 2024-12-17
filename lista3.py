lst = [5 , 4 ,3 , 11 , 32 , 33]
acumulador = 0
indice = 0
while(indice < len(lst)):
    acumulador = acumulador + lst[indice]
    indice = indice + 1
print(acumulador)