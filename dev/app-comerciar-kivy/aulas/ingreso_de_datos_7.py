"""
Ingreso de datos

Es el medio mediante el ual la información es enviada hacia dentro de la aplicacioón
"""

#Mostrar en pantalla Login, en espera de que el usuario ingrese un valor
login = input("Login:")
#Mostrar en pantalla Password, en espera de que el usuario ingrese un valor
password = input("Password:")
print(login)
print(password)
#Leemos lo que el usuario escribió y lo imprimimos
print("El usuario es: %s, y el password es: %s" %(login, password))