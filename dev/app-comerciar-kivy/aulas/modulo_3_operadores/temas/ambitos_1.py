"""
Ámbitos

Descripción: Podemos acceder a variables y/o métodos que se encientran en el mismo bloque de instrucción y en
            los bloques de instrucción que lo precede.
"""

#Identación 1 bloque de instrucción 1 (Ambito 1)
a = 1
b = 2

def suma_num(var1, var2):
    # Identación 2 bloque de instrucción 2 (Ambito 2)
    s = var1+var2
    return s

def imprime(x_veces):
    #Identación 2 bloque de instrucción 3 (Ambito 3)
    for i in range(x_veces):
        #Identación 3 bloque de instrucción 4 (Ambito 4)
        print(i)

print(suma_num(a,b))
imprime(5)