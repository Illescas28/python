"""
Toma de desiciones

Descripción Son acciones utilizadas para alterar el flujo del programa
"""
#Ejemplo 1
if(True):
    HacerAlgo = 0

# Ejemplo 2
if(True):
    HacerAlgo2 = 0
else:
    HacerAquello2 = 0

# Ejemplo 3
if(True):
    HacerAlgo3 = 0
elif(True):
    HacerAquello3 = 0

#Practica
accion = int(input("Digite '1' para si o digite '2' para no: "))
if(accion == 1):
    print("Usted dijo que si")
else:
    if(accion == 2):
        print("Usted dijo que no")
    else:
        print("Usted no digito ni 1 ni 2")