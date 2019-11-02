"""
Atribución condicional

Descripción: Es una estructura utilizada para simplificar el código,
cuyo valor a ser atribuido será aquél que satisfaga a la codición
"""

x = 10
texto = "si" if x == 10 else "no"
print(texto)

num1 = int(input("Digite un número: "))
s = "par" if num1 % 2 == 0 else "impar"
print("El número digitado es:", s)