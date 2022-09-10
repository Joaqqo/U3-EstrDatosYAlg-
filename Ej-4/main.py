from ListaS import ListaS
import os

def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n 1-Ver la lista completa ')
        print('\n 2-Cantidad de mujeres en un cargo ingresado')
        print('\n 3-Cantidad de agentes en un cargo, año y materia ingresada')
        print('\n 4- Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            lista.Recorrer()
        if(opcion == 2):
            carg=input("Ingrese el cargo que desea buscar:  ")
            lista.RecorrerB(carg)
        if(opcion == 3):
            carg=input("Ingrese el cargo: ")
            mate=input("Ingrese la materia:  ")
            anio=int(input("Ingrese el año:  ")) #El año no me lo toma
            total=lista.RecorrerD(carg, anio, mate)
            print("La cantidad de agentes designados en los datos ingresados es: {}" .format(total))
        if(opcion == 4):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')


if __name__ == '__main__':
    lista=ListaS(5)
    lista.manejadorArchivo()
    menu()
