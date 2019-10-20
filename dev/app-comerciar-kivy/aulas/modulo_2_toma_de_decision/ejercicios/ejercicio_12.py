#12) Realice un algoritmo que pida un valor numérico. Seguidamente, verifique si el número es entero o decimal.
num = input("Introduce un número: ")

es_entero = False
try:
    int(num)
    es_entero = True
except ValueError:
    es_entero = False
    try:
        float(num)
        es_entero = False
    except ValueError:
        es_entero = True

if(es_entero):
    print("El tipo de valor es enteo")
else:
    print("El tipo de valor es decimal")