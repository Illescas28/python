"""
Instrucción continue

Descripción: Es la instrucción que interrumpe la ejecución de un único ciclo
"""

print()
print("Inicio")
i = 0
while (i<10):
    i += 1
    if(i%2==0):
        continue
    print(i)
else:
    print("else")
print("fin")