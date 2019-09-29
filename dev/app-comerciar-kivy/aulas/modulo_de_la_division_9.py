#Si deseamos obtener el resto de una división, utilizaremos el simbolo porcentaje "%"
print(3%2)
print(4%2)
print(5%2)
print(7%3.1)

#Tip:  Sirve para saber si un numero es par o impar
print(900%100==0)

#Ejercicio practico:
num1 = float(input("Digite un número: "))
num2 = float(input("Digite otro número: "))

division = num1 / num2
resto = num1 % num2

print()
print(num1, "dividido por:", num2, "es igual a:", division)
print("El resto de la división entre:", num1, "y", num2, "es:", resto)
