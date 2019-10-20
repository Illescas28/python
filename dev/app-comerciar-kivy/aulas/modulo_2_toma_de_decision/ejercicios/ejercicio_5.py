#5) Realice un algoritmo que pida la edad del usuario y la edad de su madre. Seguidamente, imprima en la pantalla la edad a la que su mamá lo tuvo.
hijo_edad = int(input("Introduce su edad: "))
madre_edad = int(input("Introduce la edad de su madre: "))
madre_edad_nacimiento_hijo = madre_edad - hijo_edad

print("La edad que tenía su madre cuando ud nacio era de %i" %(madre_edad_nacimiento_hijo))