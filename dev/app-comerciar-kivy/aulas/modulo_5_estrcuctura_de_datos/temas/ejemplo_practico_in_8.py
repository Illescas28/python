
# Ejemplo 1
a = 10
b = 25
c= 66

x = int(input("Digite un número: "))

# if (x == a or x == b or x == c):
if (x in [a, b, c]):
    print("Esta contenido.")
else:
    print("No está contenido.")

# Ejemplo 2

colores =  ["azul", "amarillo", "rojo", "blanco"]

while True:
    color = input("Digite el nombre de un color, "
                  "0 para salir del programa: ")
    if(color=="0"):
        break
    elif color in colores:
        print("Este color está contenido!")
    else:
        print("Este color no está contenido!")
    print()



