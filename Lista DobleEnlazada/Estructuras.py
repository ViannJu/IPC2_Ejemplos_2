class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.end = None

    def añadirNodoPrincipio(self, dato):
        nuevoNodo = Nodo(dato)

        #Validamos si la lista esta vacia
        if self.head == None:
            print("Ingresando nodo con lista vacia")
            self.head = nuevoNodo
            self.end = nuevoNodo
        
        #Si por lo menos hay un nodo, insertamos al inicio
        else:
            print("Insertando nodo al principio")
            self.head.anterior = nuevoNodo
            nuevoNodo.siguiente = self.head
            self.head = nuevoNodo

    def añadirNodoFinal(self, dato):
        nuevoNodo = Nodo(dato)

        #insertamos si la lista esta vacia
        if self.head == None:
            print("Ingresando nodo con lista vacia")
            self.head = nuevoNodo
            self.end = nuevoNodo

        #si por lo menos hay un nodo, insertamos al final
        else:
            print("Insertando nodo al final")
            self.end.siguiente = nuevoNodo
            nuevoNodo.anterior = self.end
            self.end = nuevoNodo


    def imprimirLista(self):
        print("*** Imprimiendo lista ***")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("Nodo:"+str(contador)+" -> "+nodoTemporal.dato)
            nodoTemporal = nodoTemporal.siguiente

        print("*** Lista Terminada ***")

    def borrarNodo(self, dato):
        #creamos un nodo temporal
        nodoTemporal = Nodo("")

        #el temporal empieza en la cabeza
        nodoTemporal = self.head

        #Mientras que el temporal no sea nulo
        while nodoTemporal != None:

            #validamos si ese nodo es el que busco
            if nodoTemporal.dato == dato:

                #Si ese nodo es la cabeza
                if nodoTemporal == self.head:
                    print("Borrando dato en la cabeza")
                    self.head = self.head.siguiente
                    nodoTemporal.siguiente = None
                    self.head.anterior = None
                #Si ese nodo es la cola
                elif nodoTemporal == self.end:
                    print("Borrando dato en la cola")
                    self.end = self.end.anterior
                    nodoTemporal.anterior = None
                    self.end.siguiente = None
                #Si no es ni la cola ni la cabeza
                else:
                    print("Borrando dato del medio")
                    nodoTemporal.anterior.siguiente = nodoTemporal.siguiente
                    nodoTemporal.siguiente.anterior = nodoTemporal.anterior
                    nodoTemporal.siguiente = nodoTemporal.anterior = None

            nodoTemporal = nodoTemporal.siguiente




    