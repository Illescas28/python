#11) Realice un algoritmo que solicite al usuario que escriba 2 números. Seguidamente, imprima el total de la división en números  decimales y el total de la división en números enteros ( es decir, sin casillas decimales).
try:
    numero_1 = int(input("Introduce un numero: "))
    numero_2 = int(input("Introduce un segundo numero: "))
    division_con_decimales = numero_1/numero_2
    division_sin_decimales = numero_1/numero_2
    print("La división con decimales y sin decimales de %i entre %i es %.2f y %.0f respectivamente" %(numero_1, numero_2, division_con_decimales, division_sin_decimales))
except ValueError:
    print("Error, introduce un número")