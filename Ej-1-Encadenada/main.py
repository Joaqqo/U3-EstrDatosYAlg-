from ListaE import ListaE
if __name__ == '__main__':
    lista=ListaE()

    for i in range(1, 8):
        lista.Insertar(i,i) #Se carga la lista
    lista.Recorrer() #Se muestra la lista
    lista.Insertar(0,1) #Se inserta en la primer posición
    lista.Recorrer()
    print(lista.Vacia()) #Devuelve False porque no está vacía
    print(lista.Recuperar(1)) #Recupera 0
    print(lista.Buscar(3)) #Devuelve el índice de donde esté el 3
    lista.Suprimir(1) #Se suprime el 0
    print(lista.PrimerElemento())
    print(lista.UltimoElemento())
    lista.Recorrer()
    print(lista.Anterior(2))
    print(lista.Siguiente(2))

