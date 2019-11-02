"""
Atribución multiple

Una forma elegante de declarar variables
"""

a = 10
b = 5
print(a)
print(b)

#invertir los valores de las variables sin nesecidad de crear una 3ra variable
a, b = b, a
print(a)
print(b)

#Atribuciones de variables en una sola linea
a,b,c = 2,4,8
print(a)
print(b)
print(c)

a,b,c = a*2, a+b+c, a*b*c
print(a)
print(b)
print(c)