#Este programa te dice tu indice de masa corporal
print("¿cuanto pesas en kg?")
peso = int(input())
print("¿cuanto mides en metros?")
altura = float(input())
IMC = peso / (altura * altura)
print("tu indice de masa corporal es", IMC)