"""
Operadores Relacionales
"""
#Práctica
numero1 = input("Digite un número: ")
numero1 = int(numero1)

numero2 = input("Digite otro número: ")
numero2 = int(numero2)

if(numero1==numero2):
    print("El numero %d es igual que el numero %d " %(numero1, numero2))
if(numero1!=numero2):
    print("El numero %d es diferente que el numero %d " %(numero1, numero2))
if(numero1<numero2):
    print("El numero %d es menor que el numero %d " %(numero1, numero2))
if(numero1>numero2):
    print("El numero %d es mayor que el numero %d " %(numero1, numero2))
if(numero1>=numero2):
    print("El numero %d es mayor o igual que el numero %d " %(numero1, numero2))
if(numero1<=numero2):
    print("El numero %d es menor o igual que el numero %d " %(numero1, numero2))