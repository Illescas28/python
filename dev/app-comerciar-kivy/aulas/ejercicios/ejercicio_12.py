#12) Realice un algoritmo que solicite al usuario la longitud y la altura de un cuadrado. Seguidamente, imprima para el usuario cuántos metros cuadrados posee el área total del cuadrado.
try:
    longitud = int(input("Introduce la longitud de un cuadrado: "))
    altura = int(input("Introduce la altura de un cuadrado: "))
    area = longitud*altura
    print("Los metros cuadrados del area son: %.2f" %(area))
except ValueError:
    print("Error, introduce un número")