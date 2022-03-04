from re import subn
from graphviz import Digraph

class Nodo:
    def __init__(self, color, fila, columna):
        self.color = color
        self.fila = fila
        self.columna = columna
        self.siguiente = None

class Lista:
    def __init__(self):
        self.head = None
        self.end = None

    def añadirNodo(self, color, fila, columna):
        nuevoNodo = Nodo(color, fila, columna)
        if self.head == None:
            self.head = nuevoNodo
            self.end = nuevoNodo
        else:
            self.end.siguiente = nuevoNodo
            #nuevoNodo.anterior = self.end
            self.end = nuevoNodo

    def imprimirLista(self):              
        print("*** Inicio de lista ***")
        print()
        nodoTemporal = Nodo("",0,0)
        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("Nodo:"+str(contador)+" -> "+nodoTemporal.color+" fila: "+nodoTemporal.fila+
            "columna: "+nodoTemporal.columna)
            nodoTemporal = nodoTemporal.siguiente
        print()
        print("*** Lista Terminada ***")


    def graficarLista(self, columnas, nuNodos):
        print("Graficando lista...")
        
        dot = Digraph('G', filename='process.dot', engine='dot', format='svg')
        dot.attr(rankdir = "TB")
        dot.node_attr.update(shape="box")
        dot.node_attr['style'] = 'filled'

        nodoTemporal = Nodo("",0,0)
        nodoTemporal = self.head

        flag = False
        contador = 0
        contSubgrap = 1
        c = Digraph('child')
        c.attr(rank='same')
        while nodoTemporal != None:

            if flag:   
                c = Digraph('child'+str(contSubgrap))
                contSubgrap += 1            
                c.attr(rank='same')
                flag = False

            contador += 1
            #depende si el nodo es 'B' o 'W'
            if nodoTemporal.color == 'B':
                c.node(str(contador), "black", color="black", group=str(contador%(columnas)))

            else:
                c.node(str(contador), "", fillcolor="white", group=str(contador%(columnas)))
            
            if contador%columnas == 0:
                dot.subgraph(c)
                flag = True
                

            nodoTemporal = nodoTemporal.siguiente

        #ahora trabajamos con el contador de 0 -> contador
        for i in range(1,contador):
            if i+columnas <= nuNodos:
                dot.edge(str(i), str(i+columnas))

            if i%columnas != 0:
                dot.edge(str(i), str(i+1))

        dot.view()