import os

def suma():
    # os.system('clear')
    print("SUMA")
    print("Escribe el primer numero:")
    i = input()
    print("Escribe el segundo numero:")
    j = input()
    print("La suma es: " + str( i + j ))
    
def resta():
    # os.system('clear')
    print("RESTA")
    print("Escribe el primer numero:")
    i = input()
    print("Escribe el segundo numero:")
    j = input()
    print("La resta es: " + str( i - j ))
    
def multiplicacion():
    # os.system('clear')
    print("MULTIPLICACION")
    print("Escribe el primer numero:")
    i = input()
    print("Escribe el segundo numero:")
    j = input()
    print("La multiplicacion es: " + str( i * j ))
    
def division():
    # os.system('clear')
    print("DIVISION")
    print("Escribe el primer numero:")
    i = input()
    print("Escribe el segundo numero:")
    j = input()
    print("La division es: " + str( i / j ))

while True:
    # os.system('clear')
    print("CALCULADORA")
    print("Pulsa el numero de la operacion que quieras realizar:")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicacion")
    print("4 - Division")
    print("5 - Cerrar")
    print("Numero: ")
    operacion = input()

    if operacion == 1:
        suma()
    elif operacion == 2:
        resta()
    elif operacion == 3:
        multiplicacion()
    elif operacion == 4:
        division()
    elif operacion == 5:
        print("Cerrando...")
        exit()
