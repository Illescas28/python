#16) Las direcciones de IP versión 4 son divididas en cinco clases: A, B, C, D y E. Las direcciones  que se encuentran en un intervalo entre 0 y 127 pertenecen a la clase A, entre 128 y 191 pertenecen a la clase B, entre 192 y 223 pertenecen a la clase C, entre 224 y 239 pertenecen a la clase D y a partir de 240 pertenecen a la clase E. Realice un algoritmo que lea el primer octeto, en el formato decimal de una dirección IP, e informe su clase.
ip = "127.0.0.1"
result = ip.split(".")
if(int(result[0]) <= 127):
    print("La direccion IP es del tipo A")
elif(int(result[0]) >= 128 and int(result[0]) <= 191):
    print("La direccion IP es del tipo B")
elif(int(result[0]) >= 192 and int(result[0]) <= 223):
    print("La direccion IP es del tipo C")
elif(int(result[0]) >= 224 and int(result[0]) <= 239):
    print("La direccion IP es del tipo D")