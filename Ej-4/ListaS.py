import numpy as np
from Designaciones import Designaciones
import csv

class ListaS:
    __incremento= 5
    __dimension= 0
    __cant= 0

    def __init__(self, dimension, incremento=10):
        self.__items=np.empty(dimension, dtype=Designaciones)
        self.__cant=0 #Cantidad
        self.__dimension= dimension #Dimension

    def Vacia(self):
        return self.__cant == 0


    def Insertar(self, dato, posicion):
        posicion=posicion-1
        if posicion >= 0 and posicion <= self.__cant: #Si la posición es mayor o igual que 0 o y si es menor o igual que la cantidad
            if self.Vacia(): #Si está vacía, lo inserta en la primer posición
                self.__items[self.__cant]=dato
            else:
                if posicion == self.__cant: #Si la posición y la cantidad es igual, entonces hay que agrandar la lista
                    self.__dimension+=self.__incremento
                    self.__items.resize(self.__dimension)
                    self.__items[posicion]=dato
                else: #Para mover los valores
                    for i in range(self.__cant-posicion+1): #Quedaría un rango desde 0 hasta por ejemplo 3 si el resultado es 4
                        self.__items[self.__cant-i+1]= self.__items[self.__cant-i] #Aca se hace el cambio
                    self.__items[posicion]=dato
            self.__cant+=1
        else:
            print("Error en la inserción.")


    def Recuperar(self, posicion):
        posicion=posicion-1
        if posicion < self.__cant and posicion >= 0:
            dato= self.__items[posicion]
        else:
            dato="Hubo un error con la posición ingresada."
        return dato


    def Recorrer(self):
        for i in range(self.__cant):
            if i < self.__cant-1:
                print(f" {self.__items[i]}, ", end="" )  #Para que quede en una sola línea
            else:
                print(f" {self.__items[i]}" ) #Para que no tome lo que sigue



    def RecorrerA(self, cargo): #Una forma de hacerlo - Inciso b)
        print("AÑO - CANTIDAD")
        for i in range(self.__cant):
            if self.__items[i].getCargo().lower() == cargo.lower():
                print(self.__items[i])

    def RecorrerB(self, cargo): #Otra forma de hacerlo - Inciso b)
        print("AÑO - CANTIDAD")
        for i in range(1, self.__cant+1):
            dato=self.Recuperar(i)
            if dato.getCargo().lower() == cargo.lower():
                print(dato)



    def RecorrerC(self, cargo, year, materia): #Una forma de hacerlo - Inciso d)
        cont=0
        for i in range(self.__cant):
            if self.__items[i].getMateria().lower() == materia.lower():
                if self.__items[i].getCargo().lower() == cargo.lower():
                    #if self.__items[i].getYear() == year: #El año no lo toma en el if por alguna razón que desconozco
                    cont+=1
        return cont

    def RecorrerD(self, cargo, year, materia): #Otra forma de hacerlo - Inciso d)
        cont=0
        for i in range(1, self.__cant+1):
            dato=self.Recuperar(i)
            if dato.getCargo().lower() == cargo.lower():
                if dato.getMateria().lower() == materia.lower():
                    # if dato.getYear() == year: #El año no lo toma en el if por alguna razón que desconozco
                    cont+= dato.getCanth() + dato.getCantm()
        return cont



    def manejadorArchivo(self): #Inciso b)
        archi=open("estadistica-designacion-magistrados-federal-nacional-por-genero.csv")
        reader= csv.reader(archi, delimiter=',')
        next(reader)
        j=1
        for i in reader:
            anio=str(i[0])
            just=str(i[1])
            carg=str(i[2])
            inst=str(i[3])
            mate=str(i[4])
            canh=int(i[5])
            canm=int(i[6])
            objeto= Designaciones(anio,just,carg,inst,mate,canh,canm)
            self.Insertar(objeto, j)
            j+=1
        archi.close()
