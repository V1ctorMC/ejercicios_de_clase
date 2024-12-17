def suma(x,y):
    resultado = x + y
    return resultado
print(suma(4, 5))

def resta(a, b):
    resultado2 = a - b
    return resultado2
print(resta(10, 5))

def multiplicacion(c, d):
    resultado3 = c * d
    return resultado3
print(multiplicacion(2, 5))

def siguiente(z):
    resultado4 = z + 1
    return resultado4
print(siguiente(1))

def mayor2(m, n):
    if (m > n):
        return m
    else:
        return n
print(mayor2(4, 8))

def mayor3(f,g,h):
    if(f > g) and (f > h):
        return f
    if(g > f) and (g > h):
        return g
    if(h > f) and (h > g):
        return h
print(mayor3(7, 9, 3))
