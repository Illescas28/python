#18) Realice un algoritmo que valide una fecha. La misma debe estar constituída por dia, mes y año. Por ejemplo, si el usuario escribe la fecha 10/8 la misma será inválida. Y en caso de que el usuario  escriba la fecha 01/10/2018, la misma debe ser considerada válida.
fecha = input("Ingrece una fecha (Ejemplo 20/10/2019): ")
dias = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
meses = ["01","02","03","04","05","06","07","08","09","10","11","12"]
if("/" in fecha):
    fecha = fecha.split("/")
    dia = fecha[0]
    if(len(dia) == 2 and dia in (dias)):
        mes = fecha[1]
        if (len(mes) == 2 and mes in (meses)):
            ano = fecha[2]
            if (len(ano) == 4):
                print("La fecha ingresada es: " + str(dia) + "/" + str(mes) + "/" + ano)
            else:
                print("Año invalido")
        else:
            print("Mes invalido, el mes debe ser de 01 al 12")
    else:
        print("Dia invalido, el dia debe ser de 01 al 31")
else:
    print("Formato invalido")