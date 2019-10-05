#9) Realice un algoritmo que solicite al usuario que informe una medida en metros. Seguidamente, convierta a esta medida de metros a centímetros y envíela a la salida estándar.
try:
    metros = float(input('Introduce el número de metros que hay entre una distancia y otra: '))
    centimetros = float(metros*100)
    print("Los metros %.1f es igual a %.2f centimetros" %(metros, centimetros))
except ValueError:
    print('Error, introduce un número')