#7) Realice un algoritmo que pida un número al usuario y verifique si el mismo es par o impar.
num = int(input("Introduce un número: "))
# obtenemos el residuo de la divición
if (num%2 == 0):
    print("El número %i es par" % (num))
else:
    print("El número %i es impar" % (num))