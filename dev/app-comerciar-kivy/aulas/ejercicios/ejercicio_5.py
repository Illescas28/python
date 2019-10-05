#5) Realice un algoritmo que solicite al usuario informar un número. Seguidamente, escriba el siguiente mensaje  "El número escrito fue:   "
try:
    numero = int(input('Introduce un número: '))
    print("El número escrito fue: %i " %(numero))
except ValueError:
    print('Error, introduce un numero entero')