from graphviz import Digraph

class nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaCircular: 
    def __init__(self):
        self.primero = None

    def insertar(self, valor):
        nuevo = nodo(valor)
        if self.primero == None:
            self.primero = nuevo
            self.primero.siguiente = self.primero
            self.primero.anterior = self.primero
        else:
            nuevo.siguiente = self.primero
            nuevo.anterior = self.primero.anterior
            self.primero.anterior.siguiente = nuevo
            self.primero.anterior = nuevo
            self.primero = nuevo
    
    def eliminar(self, valor):
        if self.primero != None:
            actual = self.primero
            while actual.valor != valor:
                actual = actual.siguiente
                if actual == self.primero:
                    return
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            if actual == self.primero:
                self.primero = actual.siguiente
    
    def imprimir(self):
        if self.primero != None:
            actual = self.primero
            while actual.siguiente != self.primero:
                print(actual.valor)
                actual = actual.siguiente
            print(actual.valor)

    def graficar(self):
        dot = Digraph('G', filename='process.dot', engine='dot', format='svg')
        dot.attr(rankdir = "TB")
        dot.node_attr.update(shape="box")
        dot.node_attr['style'] = 'filled'

        contador = 0
        c = Digraph('child')
        c.attr(rank='same')

        if self.primero != None:
            actual = self.primero
            while actual.siguiente != self.primero:
                contador += 1
                c.node(str(contador), actual.valor)#, color="black")
                
                actual = actual.siguiente
            contador += 1
            c.node(str(contador), actual.valor)
        
        dot.subgraph(c)

        for i in range(1,contador):
            dot.edge(str(i), str(i+1))
        
        for i in range(contador, 1, -1):
            dot.edge(str(i), str(i-1))

        dot.edge(str(1), str(contador))
        dot.edge(str(contador), str(1))

        dot.view()



