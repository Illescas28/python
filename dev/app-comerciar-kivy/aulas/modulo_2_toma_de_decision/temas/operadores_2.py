"""
Operadores
"""
#Práctica
edad = int(input(("Ingresa tu edad:")))
if(edad<=0):
    print("Su edad no puede ser menor o igual a 0")
else:
    if(edad>150):
        print("Su edad no puede ser mayor a 150")
    else:
        if (edad < 18):
            print("Ud necesita tener mas de 18 años")

#Simplificando coóigo con elif
if(edad<=0):
    print("Su edad no puede ser menor o igual a 0")
elif(edad>150):
    print("Su edad no puede ser mayor a 150")
elif (edad < 18):
    print("Ud necesita tener mas de 18 años")