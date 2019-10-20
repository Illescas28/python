#13) Realice un algoritmo que lea tres números e imprima en la pantalla al mayor de ellos.
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
num3 = int(input("Introduce otro número: "))

if(num1 > num2 and num1 > num3):
    print("El número %i es mayor que el número %i y el número %i" %(num1, num2, num3))
elif(num2 > num1 and num2 > num3):
    print("El número %i es mayor que el número %i y el número %i" %(num2, num1, num3))
elif(num3 > num1 and num3 > num2):
    print("El número %i es mayor que el número %i y el número %i" %(num3, num1, num2))