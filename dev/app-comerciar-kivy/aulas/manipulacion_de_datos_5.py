"""
Manipulación de datos

Nota:
Python es un lenguaje de tipificación dinámica
"""

num_int = 5
num_dec = 7.3
val_str = "qualquier texto"

#print puede trabajar con cualquier tipo de dato
print(num_int)

#Aqui tenemos 2 tipos de datos diferentes, para concatenar, utilizamos ',' (la coma). La coma agrega un espacio implicito en la impresion del resultado
print("El valor es:", num_int)

#Para agregar un marcador en nuestro string, utilizamos el signo % y el tipo de dato. Ejemplo (%i = %variable de tipo entero) y no requiere la coma, en su lugar utilizaremos %
print("El valor es: %i" %num_int)

#Convertir el tipo de dato
print("El valor es:", str(num_int))

#Tambien podemos concatenar con + pero no agrega un espacio y debes especificar el mismo tipo de dato en la concatenacion
print("El valor es:" + str(num_int))


#Concatenacion de String
print("Concatenando string:", val_str)
print("Concatenando string: %s" %val_str)
print("Concatenando string: " + val_str)