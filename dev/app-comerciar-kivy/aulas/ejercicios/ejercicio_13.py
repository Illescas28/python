#13) Realice un algoritmo que solicite al usuario informar una cantidad de días, horas, minutos y segundos. Seguidamente, convierta todo a segundos.
try:
    dias = int(input("Introduce dias: "))
    horas = int(input("Introduce horas: "))
    minutos = int(input("Introduce minutos: "))
    segundos = int(input("Introduce segundos: "))

    area = (dias*24*60*60)+(horas*60*60)+(minutos*60)+segundos
    print("Los metros cuadrados del area son: %.2f" %(area))
    area = (dias*86400)+(horas*3600)+(minutos*60)+segundos
    print("Los metros cuadrados del area son: %.2f" %(area))
except ValueError:
    print("Error, introduce un número")