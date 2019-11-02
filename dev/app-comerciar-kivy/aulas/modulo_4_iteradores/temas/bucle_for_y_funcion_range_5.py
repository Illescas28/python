"""
Bucle for y función range
"""

print(list(range(10)))

#Inicializamos el conteo en 1
print(list(range(1, 10)))

#Inicializamos el conteo en 0 y el intervalo será de 10 en 10 unidades
print(list(range(0, 100, 10)))

#Inicializamos el conteo en 100 y el intervalo será de -3 unidades
print(list(range(100, 0, -3)))

#Inicializamos el conteo en -100 y el intervalo será de 3 unidades (imprimimos números negativos)
print(list(range(-100, 0, 3)))

for i in range(-10, 0, 1):
    print(i)