from Nodo import Nodo

class ListaEC:
    __inicio = None
    __tope = 0

    def __init__(self):
        self.__inicio = None
        self.__tope = 0

    def Vacia(self):
        return self.__tope == 0


    def Insertar(self,dato):
        anterior=None
        nodo = Nodo(dato)
        if self.Vacia():
            self.__inicio = nodo
        else:
            aux = self.__inicio
            while aux != None and aux.getDato() < dato: #Si es distinto de None y el dato de Aux es menor al dato, que continue hasta que se posicione en donde se tiene que estar
                anterior = aux
                aux = aux.getSiguiente()
            if aux == None: #En el caso de que el número ingresado sea el mayor de todos
                anterior.setSiguiente(nodo) #Se inserta en la última posición
            elif aux == self.__inicio: #En el caso de que sea en la primer posición
                nodo.setSiguiente(aux)
                self.__inicio = nodo
            else: #En alguna posición del "medio"
                nodo.setSiguiente(aux)
                anterior.setSiguiente(nodo)
        self.__tope += 1

    def Recorrer(self):
        aux= self.__inicio
        for i in range(self.__tope):
            if i < self.__tope-1:
                print(f" {aux.getDato()}, ", end="") #Para que quede en una sola línea
                aux=aux.getSiguiente()
            else:
                print(f"{aux.getDato()}")

    def Recuperar(self, posicion):
        posicion=posicion-1
        if posicion < self.__tope and posicion >= 0: #Posicion < self.__tope pq el tope siempre es uno más
            aux= self.__inicio
            i=0
            while i < posicion:
                aux= aux.getSiguiente()
                i+=1
            dato= aux.getDato()
        else:
            dato="Error en la posición ingresada" #Esto puede traer problemas -> Revisar
        return dato

    def Buscar(self, dato): #Devuelve el indice
        i=0
        aux= self.__inicio
        indice= None
        bandera= False
        while aux != None and not bandera:
            if aux.getDato() == dato: #Si lo encuentra, bandera=True para cortar la iteración
                bandera=True
            else: #En caso de q no lo encuentre para continuar la iteración
                aux=aux.getSiguiente()
                i+=1
        if aux != None:
            indice = i
        else:
            indice="Error en el dato ingresado"
        return indice

    def Suprimir(self, posicion):
        anterior=None
        posicion=posicion-1
        #aux=None
        if posicion < self.__tope and posicion >= 0:
            if posicion == 0: #Si la posición es 0 entonces
                aux= self.__inicio #Auxiliar toma el valor de inicio
                self.__inicio= aux.getSiguiente() #Y el inicio la del siguiente
            else:
                aux= self.__inicio
                i= 0
                while i != posicion:
                    anterior=aux #Anterior es igual a Auxiliar
                    aux=aux.getSiguiente() #Y aux toma el valor del que le sigue
                    i+=1
                anterior.setSiguiente(aux.getSiguiente()) #Seteamos el siguiente de anterior como el siguiente de auxiliar
            self.__tope -= 1
        #return aux

    def PrimerElemento(self):
        return self.__inicio.getDato()

    def UltimoElemento(self): #Revisar si funciona
        anterior= None
        aux= self.__inicio
        while aux != None: #aux != None
            anterior= aux
            aux= aux.getSiguiente()
        return anterior.getDato()

    def Siguiente(self, posicion):
        posicion=posicion-1
        if posicion < self.__tope and posicion >= 0:
            aux=self.__inicio
            i=0
            while i < posicion+1:
                aux= aux.getSiguiente()
                i+=1
            dato= hex(id(aux.getDato())) #Para que devuelva la dirección en hexadecimal
        else:
            dato="Error con la posición ingresada."
        return dato

    def Anterior(self, posicion):
        posicion=posicion-1
        if posicion < self.__tope and posicion >= 0:
            aux= self.__inicio
            i=0
            while i < posicion-1:
                aux= aux.getSiguiente()
                i+=1
            dato=hex(id(aux.getDato())) #Para que devuelva la dirección en hexadecimal
        else:
            dato="Error con la posición ingresada."
        return dato
