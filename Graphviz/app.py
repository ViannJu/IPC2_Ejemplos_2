from Lista import Lista

lista = Lista()

def guardarPatron(patron, filas, columnas):
    #recorremos la cadena del string guardandolo en la lista
        for i in range(0, filas):
            for j in range(0, columnas):
                letra = patron[(i*columnas)+j]
                row = str(i)
                col = str(j)
                print("letra: "+letra+" fila: "+row+" columna: "+col)
                lista.añadirNodo(letra, row, col)

if __name__ == '__main__':
    guardarPatron("BWBWWBWB", 2, 4)
    #lista.imprimirLista()
    lista.graficarLista(4, 8)#columnas, elementos
