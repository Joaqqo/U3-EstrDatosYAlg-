import numpy as np
class ListaS:
    __incremento= 5
    __dimension= 0
    __cant= 0

    def __init__(self, dimension, incremento=5):
        self.__items=np.empty(dimension, dtype=int)
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
                    for i in range(self.__cant-posicion+1): 
                        self.__items[self.__cant-i+1]= self.__items[self.__cant-i] #Aca se hace el cambio
                    self.__items[posicion]=dato
            self.__cant+=1
        else:
            print("Error en la inserción.")

    def Suprimir(self, posicion):
        posicion=posicion-1
        if posicion < self.__cant and posicion >= 0: #Para que no ingresen una posición errónea
            if self.Vacia():
                print("Lista vacía")
            else:
                for i in range(posicion, self.__cant-1): #Rango entre la posición ingresada y la cantidad menos 1
                    self.__items[i]= self.__items[i+1] #Movemos
                self.__cant -= 1
        else:
            print("Error con la posición ingresada.")



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



    def Siguiente(self, posicion):
        posicion=posicion-1
        if posicion < self.__cant-1 and posicion >= 0: #tope-1 y posicion >= 0 estan porque sino tira error
            dato= hex(id(self.__items[posicion+1])) #Para que devuelva la dirección en hexadecimal
        else:
            dato="Hubo un error con la posición ingresada."
        return dato

    def Anterior(self, posicion):
        posicion=posicion-1
        if posicion < self.__cant and posicion > 0:
            dato= hex(id(self.__items[posicion-1])) #Para que devuelva la dirección en hexadecimal
        else:
            dato="Hubo un error con la posición ingresada."
        return dato

    def PrimerElemento(self):
        if not self.Vacia():
            return self.__items[0]
        else:
            print("La lista esta vacía")

    def UltimoElemento(self):
        if not self.Vacia():
            return self.__items[self.__cant-1]
        else:
            print("La lista esta vacía")

    def Buscar(self, dato): #Retorna el índice donde está el dato ingresado
        bandera= False
        indice= None
        i= 0
        while i <= self.__cant and not bandera:
            if self.__items[i] == dato:
                bandera= True
            else:
                i+=1
            if i < self.__cant: #!!!
                indice= i
        return indice
