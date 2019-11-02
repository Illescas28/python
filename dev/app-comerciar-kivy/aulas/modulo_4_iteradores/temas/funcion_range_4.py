"""
Función range

Estructura:

range ([start], stop[, step])
"""

range (0,10,2)
print(range(0,10,2))

lista = list(range(0,10,2))
print(lista)

lista = list(range(0,10,1))
print(lista)

#Por defecto inicia la iteración en 0 y el step es uno a uno
lista = list(range(10))
print(lista)
