#14) Realice un algoritmo que lea tres números e imprímalos en orden creciente.
num1 = 30
num2 = 35
num3 = 80

if(num1 < num2 and num1 < num3):
    if(num2 < num3):
        print("%i %i %i" %(num1, num2, num3))
    elif(num3 < num2):
        print("%i %i %i" %(num1, num3, num2))
if(num2 < num1 and num2 < num3):
    if(num1 < num3):
        print("%i %i %i" %(num2, num1, num3))
    elif(num3 < num1):
        print("%i %i %i" %(num2, num3, num1))
if(num3 < num1 and num3 < num2):
    if(num2 < num1):
        print("%i %i %i" %(num3, num2, num1))
    elif(num1 < num2):
        print("%i %i %i" %(num3, num1, num2))
