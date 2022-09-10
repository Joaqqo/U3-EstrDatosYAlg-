from ListaEC import ListaEC
if __name__ == '__main__':
    lista=ListaEC()

    for i in range(1, 8):
        lista.Insertar(i) #Se carga la lista
    lista.Recorrer() #Se muestra la lista
    lista.Insertar(0)
    lista.Insertar(11)
    lista.Recorrer()
    lista.Insertar(7)
    lista.Recorrer()
    print(lista.Recuperar(2))
    print(lista.Buscar(11))
    lista.Suprimir(8)
    lista.Recorrer()
    print(lista.PrimerElemento())
    print(lista.UltimoElemento())
    print(lista.Anterior(2))
    print(lista.Siguiente(2))

