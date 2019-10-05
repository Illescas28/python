#6) Realice un algoritmo que solicite al usuario informar 3 números. Seguidamente, sume los valores y envíe a la salida estándar la siguiente frase "La suma total es:  ".
try:
    numero_1 = int(input('Introduce un número: '))
    numero_2 = int(input('Introduce un segundo número: '))
    numero_3 = int(input('Introduce un tercer número: '))
    total = numero_1 + numero_2 + numero_3
    print("La suma total es: %i " %(total))
except ValueError:
    print('Error, introduce un numero entero')