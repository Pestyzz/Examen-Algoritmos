import numpy as np
from datetime import date

""" FUNCIONES DEL PROGRAMA """
def options():
    while True:
        try:
            userOption = int(input("1.Comprar Entradas\n2.Mostrar Ubicaciones Disponibles\n3.Ver listado de asistentes\n4.Mostrar ganancias totales\n5.Salir\n>>Ingrese un dígito: "))
            
            if userOption in range(1, 6):
                return userOption
            else:
                print("Opción inválida.")
        except ValueError:
            print("Caracter inválido.")    

def user_input(message, cantEntradas=False, fila=False, columna=False, run=False):
    while True:
        try:
            userInput = input(message)
            #Validación ingreso Entradas
            if cantEntradas == True:
                if userInput.isdigit() == True:
                    userInput = int(userInput)
                else:
                    raise ValueError
                if userInput < 1 or userInput > 3:
                    print("Solamente cantidades entre 1 y 3.")
                    continue
            #Validación ingreso Fila
            if fila == True:
                if userInput.isdigit() == True:
                    userInput = int(userInput)
                else:
                    raise ValueError
                if userInput < 1 or userInput > 10:
                    print("Fila no existente.")
                    continue
            #Validación ingreso Columna
            if columna == True:
                if userInput.isdigit() == True:
                    userInput = int(userInput)
                else:
                    raise ValueError
                if userInput < 1 or userInput > 10:
                    print("Columna no existente.")
                    continue
            #Validación ingreso RUN
            if run == True:
                if userInput[2] != "." or userInput[6] != "." or userInput[10] != "-":
                    print("Formato inválido.")
                    continue
                elif userInput[0:1].isdigit() != True or userInput[3:5].isdigit() != True or userInput[7:9].isdigit() != True:
                    raise ValueError
                elif userInput[-1] not in ['0','1','2','3','4' ,'5','6','7','8','9','K','k']:
                    raise ValueError

            return userInput
        except ValueError:
            print("Caracter inválido.")

def comprar_entradas():
    while True:
        cantEntradas = user_input("Ingrese la cantidad de entradas que desea: ", cantEntradas=True)
        
        mostrar_ubi()
        
        print("-Platinum, $120.000. (Asientos del 1 al 20).\n-Gold, $80.000. (Asientos del 21 al 50).\n-Silver, $50.000. (Asientos del 51 al 100.).\n")

        for i in range(cantEntradas):
            fila = user_input("Ingrese la fila: ", fila=True)
            columna = user_input("Ingrese la columna: ", columna=True)
            if matrizUbi[fila-1, columna-1] == "X":
                print("Asiento no disponible.\n")
            else:
                matrizUbi[fila-1, columna-1] = "X"
                run = user_input("Ingrese RUN (XX.XXX.XXX-X): ", run=True)
                run = run.replace(".", "").replace("-", "").replace(run[-1], "")
                run = int(run)
                asistente = [run, fila, columna]
                listaAsistentes.append(asistente)
                listaRunAsis.append(run)
            print("Operación finalizada correctamente...")
        return

def mostrar_ubi():
    print(matrizUbi)
    print("")

def lista_asis():
    for dato in listaAsistentes:
        for run in listaRunAsis:
            if dato[0] == run:
                print(f"RUN: {run:1d} | Fila: {dato[1]:1d} | Columna: {dato[2]:1d}")
                print("--------------+---------+----------")

def mostrar_ganancias():
    cantP = int(0)
    cantG = int(0)
    cantS = int(0)

    for fila in range (0, 2):
        for columna in range(10):
            if matrizUbi[fila, columna] == "X":
                cantP += 1   
    for fila in range(2, 5):
        for columna in range(10):
            if matrizUbi[fila, columna] == "X":
                cantG += 1  
    for fila in range(5, 10):
        for columna in range(10):
            if matrizUbi[fila, columna] == "X":
                cantS += 1

    cantTotal = cantP + cantG + cantS
    sumTotal = cantP * 120000 + cantG * 80000 + cantS * 50000

    print(" Tipo Entrada      | Cantidad | Total")
    print("-------------------+----------+----------")
    print(f" Platinum $120.000 | {cantP:5d}    | {cantP * 120000:3d}")
    print("--------------+---------+---------------")
    print(f" Gold $80.000      | {cantG:5d}    | {cantG * 80000:3d}")
    print("--------------+---------+---------------")
    print(f" Silver $50.000    | {cantS:5d}    | {cantS * 50000:3d}")
    print("--------------+---------+---------------")
    print(f" TOTAL             | {cantTotal:5d}    | {sumTotal:3d}")

def salir():
    print(f"Saliendo...\nBastián Ñiripil\n{date.today}")
    menu = 0
    return menu

""" PROGRAMA PRINCIPAL """
matrizUbi = np.arange(1, 101, dtype=object).reshape(10, 10)

listaRunAsis = []
listaAsistentes = []

menu = 1
while menu == 1:
    print("VENTA ENTRADAS CONCIERTO VIP 'MICHAEL JAM'")
    userOption = options()
        
    match userOption:
        case 1:
            comprar_entradas()
        case 2:
            mostrar_ubi()
        case 3:
            lista_asis()
        case 4:
            mostrar_ganancias()
        case 5:
            menu = salir()

# LINK GITHUB EXÁMEN: 