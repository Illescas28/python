#4) Realice un algoritmo que solicite al usuario informar un número. Seguidamente, almacene a este número en una variable. Por último, envíe a ese número a la salida estándar.
try:
    numero = int(input('Introduce un número: '))
    print(numero)
except ValueError:
    print('Error, introduce un numero entero')