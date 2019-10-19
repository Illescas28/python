"""
Operadores Lógicos

Tienen la capacidad de unir expresiones lógicas y asi formar una nueva expresión

and (y)
or (o)
not (negacioó)
is (es)
is not (no es)
in (contiena)
not in (no contiene)
"""

a = 2
b = 4

if(a<b and a==b):
    print("a es menor que b y a es igual que b")
if (a > b or a < b):
    print("a es mayor que b ó a es menor que b")
if (not(a > b or a < b)):
    print("a es mayor que b ó a es menor que b")

#Tipo de dato con "type"
if(type(a) is int):
    print("El tipo de dato de a es entero")
if(type(2.0) is int):
    print("El tipo de dato no es entero")
if(type(2.0) is float):
    print("El tipo de dato de a es flotante")



