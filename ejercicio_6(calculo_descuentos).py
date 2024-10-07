#Este programa aplica un descuento a elegir ente 5%,10% o 20%
print("¿Cual es el precio de tu producto?")
precio = float(input())
print("¿Quieres aplicar un descuento del 5,10 o 20%?")
descuento = int(input())
preciofinal = precio * (1 - descuento/100)
print("Aplicando un descuento de", descuento,"%, el precio del producto será de", preciofinal, "euros")