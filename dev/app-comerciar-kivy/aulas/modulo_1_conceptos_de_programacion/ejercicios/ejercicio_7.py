#7) Realice un algoritmo que solicite al usuario informar 2 números. Seguidamente, sume los valores y envíe a la salida estándar la siguiente frase: "La suma entre <X> e <Y> es igual a <total>"
try:
    numero_1 = int(input('Introduce un número: '))
    numero_2 = int(input('Introduce un segundo número: '))
    total = numero_1 + numero_2
    print("La suma entre %i y %i es igual a %i" %(numero_1, numero_2, total))
except ValueError:
    print('Error, introduce un numero entero')
