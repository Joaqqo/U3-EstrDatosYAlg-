from ListaSC import ListaSC
if __name__ == '__main__':
    lista=ListaSC(1)

    for i in range(1, 8):
        lista.Insertar(i) #Se insertan los datos del 1 al 7
    lista.Recorrer() #Se muestra la lista
    lista.Insertar(0) #Se inserta el dato 0
    lista.Recorrer() #Se muestra la lista
    lista.Suprimir(5) #Se suprime la posición 5
    lista.Recorrer()
    print(lista.Recuperar(5)) #Se recupera la posición 5
    print(lista.Siguiente(5))
    print(lista.Anterior(5))
    print(lista.UltimoElemento())
    print(lista.PrimerElemento())
    print(lista.Buscar(5)) #Se busca el índice de donde esté el dato 5
