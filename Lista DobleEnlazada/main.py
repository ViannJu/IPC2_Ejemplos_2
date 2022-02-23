import Estructuras

listaDoble = Estructuras.ListaDoble()
listaDoble.añadirNodoPrincipio("Fresa")
listaDoble.añadirNodoPrincipio("Vainilla")
listaDoble.añadirNodoPrincipio("Chocolate")
listaDoble.añadirNodoPrincipio("Pistacho")

#listaDoble2 = Estructuras.ListaDoble()
#listaDoble2.añadirNodoFinal("Fresa")
#listaDoble2.añadirNodoFinal("Vainilla")
#listaDoble2.añadirNodoFinal("Chocolate")
#listaDoble2.añadirNodoFinal("Pistacho")

if __name__ == '__main__':
    listaDoble.imprimirLista()
    print("***  Espacio  ***")
    listaDoble.borrarNodo("Vainilla")
    listaDoble.imprimirLista()
    print("***  Espacio  ***")
    #y cualquier otra instrucción