"""
Bloques de instrucción
"""
#La Indentacion es la determinación de los bloques de instrucción
if(True):
    print("Imprime un texto")
    print("Imprime un texto")
    print("Imprime un texto")
    print("Imprime un texto")
if(False):
    print("No se imprime")
    print("No se imprime")
    print("No se imprime")
    print("No se imprime")

#Definicion de bloques de instrucción dentro de bloques de instrucción
a = 25
if(True):
    a = 50
    if(False):
        b = 50
    a = 40

#Practicas
num1 = int(input("Digite un número: "))
if(num1 > 10):
    print("El valor es mayor a 10")
    if(num1<=15):
        print("El valor es menor o igual a 15")
    else:
        if(num1<=50):
            print("El valor es menor a 10 y menor o igual que 50")
        else:
            print("El valor es mayor que 50")
else:
    if(num1>5):
        print("El valor es menor que 10 y mayor que 5")
        if(num1==7):
            print("El valor es 7")
    else:
        print("El valor es menor a 5")