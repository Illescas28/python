#8) Realice un algoritmo que solicite las notas de las 4 pruebas semestrales al usuario. Seguidamente, calcule la media y envíe el valor resultante a la salida estándar:
try:
    nota_1 = int(input('Introduce la calificación obtenida en Algebra: '))
    nota_2 = int(input('Introduce la calificación obtenida en Trigonometria: '))
    nota_3 = int(input('Introduce la calificación obtenida en Calculo Diferencia e Integral: '))
    nota_4 = int(input('Introduce la calificación obtenida en Programación I: '))
    promedio = float((nota_1 + nota_2 + nota_3 + nota_4)/4)
    print("El promedio es %f" % (promedio))
    print("El promedio es %.2f" % (promedio)) #Delimitamos a 2 las decimales
except ValueError:
    print('Error, introduce un numero entero')