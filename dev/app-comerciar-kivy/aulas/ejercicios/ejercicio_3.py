#3) Realice un algoritmo que solicite el nombre y la edad del usuario., seguidamente, envíe la siguiente frase a la consola: "El nombre es <nombre> y su edad es <edad>"
usuario_nombre = input('Ingrese su nombre: ')
try:
    usuario_edad = int(input('Ingrese su edad: '))
    print("El nombre es %s y su edad es %i " %(usuario_nombre, usuario_edad))
except ValueError:
    print('Error, introduce un numero entero')
