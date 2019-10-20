#8) Realice un algoritmo que pida dos números. Primero, imprima al mayor de ellos y, seguidamente imprima al menor de ellos.
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
if(num1 > num2):
    print("El número %i es mayor que el número %i" %(num1, num2))
else:
    print("El número %i es mayor que el número %i" %(num2, num1))