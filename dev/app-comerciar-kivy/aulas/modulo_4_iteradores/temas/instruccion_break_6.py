"""
Instrucción break

Es la instrucción que interrumpe la ejecuciñon del cucle de repetición en el cual se enuentra contenida.
"""

print("Antes de entrar al bucle")
for item in range(10):
    print(item)
    if(item==6):
        break
print("Despues de haber entrado al bucle")