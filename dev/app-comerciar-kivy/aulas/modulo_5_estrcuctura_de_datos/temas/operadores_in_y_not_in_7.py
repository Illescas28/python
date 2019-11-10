

#Conocer si un parametro o valor se encuentra contenido en una Tupla
2 in (1,2,3,4,5)
#el valor resultante sera True ya que 2 si se encuentra dentro de la Tupla
6 not in (1,2,3,4,5)
#el valor resultante sera True ya que 6 no se encuentra dentro de la Tupla
1 in range(1,6,)
#Conocer si 1 se encuentra dentro de las posiciones 1 al 6 con intervalos de 1 en 1

x = range(1,6)
if 3 in x:
    print("Contenido")
else:
    print("No contenido")


