#Crear menú con tres opciones: 
#1. Opcion 1: Temperaturas
#2. Opcion 2: Datos de Personas
#3. Opción 3: Salir 
import os
import math

def Temperaturas():
    print("---- TEMPERATURAS ----")
    suma=0
    tm=int(input("Digite temperaturas a ingresar: "))
    for x in range(tm):
        temp=float(input("Digite temperatura: "))
        suma=suma+temp

    print("El promedio de las temperaturas ingresadas: " ,round((suma/tm),2))

    pausa=input("Presione cualquier tecla para continuar")

def Personas():
    print("---- DATOS DE PERSONAS ----")
     #ingresar para n personas donde n es un numero ingresado por teclado: 
    #nombre y edad. Mostrar cuantas personas son mayores de edad y cuantas son menores de edad
    #subir a github la segunda version de lo programado con el siguiente commit:
    #"Se agrego opcion 2 al menu de python"
    may=0
    men=0
    pr=int(input("Cuantas personas desea ingresar?: "))
    for x in range(pr):
        nom=input("Ingrese nombre de la persona: ")
        edad=int(input("Ingrese edad de la persona: "))

        if(edad >= 18):
            may += 1
        else:
            men += 1
        
    print("El total de personas mayores de edad es: " + str(may))
    print("El total de personas menores de edad es: " + str(men))

    pausa=input("Presione cualquier tecla para continuar")

seguir=True
while seguir:
    os.system('cls')
    print("1. Temperatura")
    print("2. Datos de Personas")
    print("3. Salir")
    op=int(input("Ingrese opción (1, 2, 3): "))
    if(op==1):
        Temperaturas()
    elif(op==2):
        Personas()
    else:
        print("Finalizar")
        break