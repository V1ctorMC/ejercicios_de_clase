
def multiplicar(a,b):
    multiplicacion = a * b
    return multiplicacion
print(multiplicar(2,3))

def multiplicar3(c,d,e):
    multiplicacion3 = c * d * e 
    return multiplicacion3
print(multiplicar3(2,3,2))

def bucle_infinito():
    no_fin = True
    while no_fin:
        respuesta = input("Dime algo:")
        if (respuesta == "hola"):
            print("has dicho hola")
        elif (respuesta == "fin"):
            no_fin = False
            
bucle_infinito()

def nota(nota):
    print("Dime tu nota del 0 al 100")
    nota = int(input())
    if (nota >= 90):
        print("sobresaliente")
    elif (nota >= 70) and (nota <= 89):
        print("notable")
    elif (nota >= 50) and (nota <= 69):
        print("aprobado")
    elif (nota < 50):
        print("suspenso")

nota(nota)