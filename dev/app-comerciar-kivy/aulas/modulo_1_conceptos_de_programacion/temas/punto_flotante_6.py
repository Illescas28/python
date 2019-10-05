num_dec = 7.3

print("Contatenando decimal", num_dec)

#Por defecto, la impresión del resultado será con 5 decimals
print("Contatenando decimal: %f" %num_dec)
#Especificar el número de decimales
print("Contatenando decimal: %.10f" %num_dec)
#Signo de adicion paraa concatenar string con float, esta instruccion marcará error
#print("Contatenando decimal: " + num_dec)
#Para concatenar, reerimos hacer un CAST con "str()"
print("Contatenando decimal: " + str(num_dec))