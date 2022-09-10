from Nodo import Nodo
from Provincia import Provincia
import csv

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
                print(f" {aux.getDato()}") #Para que quede en una sola línea
                aux=aux.getSiguiente()
            else:
                print(f"{aux.getDato()}")

    def manejadorArchivo(self):
        archi=open("superficie-afectada-por-incendios-forestales-en-el-pais.csv")
        reader= csv.reader(archi, delimiter=';')
        next(reader)
        j=1
        for i in reader:
            nom=str(i[3])
            sup=float(i[6])
            objeto= Provincia(nom, sup)
            self.Insertar(objeto)
            j+=1
        archi.close()





