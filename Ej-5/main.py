from ListaS import ListaS
if __name__ == '__main__':
    lista=ListaS(6)
    lista.Insertar(10,1)
    lista.Insertar(5,2)
    lista.Insertar(7,3)
    lista.Insertar(5,4)
    lista.Insertar(2,5)
    lista.Insertar(10,6)
    lista.Recorrer() #Se muestra la lista
    lista.Cambio()
    lista.Recorrer()
