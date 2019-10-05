#10) Realice un algoritmo que calcule el cubo y el cuadrado de un determinado número:
try:
    numero = int(input("Introduce un número: "))
    numero_al_cubo = float(numero**3)
    numero_al_cuadrado = float(numero**2)
    print("El cubo y el cuadrado de %i es: %.2f y %.2f respectivamente." %(numero, numero_al_cubo, numero_al_cuadrado))
except ValueError:
    print("Error, introduce un número")