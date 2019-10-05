#14) Realice un algoritmo que solicite al usuario informar el valor de una compra.Seguidamente, aplique un 10% de descuento e imprima en la pantalla tanto el valor total como el valor con el descuento aplicado.
try:
    compra = int(input("Introduce el valor del producto comprado: "))
    diez_porciento = compra - (compra * 0.10)

    print("El producto costó %.2f menos el 10 porciento costó %.2f" %(compra, diez_porciento))
    print("El producto costó " + str(compra) + " menos el 10% costó " + str(diez_porciento))
except ValueError:
    print("Error, introduce un número")