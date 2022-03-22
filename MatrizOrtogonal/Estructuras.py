from graphviz import Digraph

class Nodo:
    def __init__(self):
        self.dato = None
        #Coordenadas
        self.posVertical = None
        self.posHorizontal =None
        #Apuntadores
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None

class MatrizOrtogonal:
    def __init__(self):
        #Creamos el nodo raiz en 0,0
        self.raiz = Nodo()
        self.raiz.posVertical = 0
        self.raiz.posHorizontal = 0

    def crearIndiceVertical(self, pos):
        # recorrer todos los nodos de manera vertical
        # creamos un temporal
        tmp = self.raiz
        while tmp != None:
            # no existe el indice; solo hay índices menores
            if tmp.abajo == None and tmp.posVertical < pos:
                # ya no hay más nodos en vertical
                # se inserta al final
                nuevo = Nodo()
                nuevo.posHorizontal = 0
                nuevo.posVertical = pos
                nuevo.arriba = tmp
                tmp.abajo = nuevo
                return tmp.abajo
            
            # indice actual es igual a el nuevo índice
            if tmp.posVertical == pos :
                # no hacer nada
                return tmp

            # indice actual es menor, pero el siguiente es mayor
            if tmp.posVertical < pos and tmp.abajo.posVertical > pos:
                # insertar un nodo en medio del nodo actual y del nodo siguiente
                nuevo = Nodo()
                nuevo.posHorizontal = 0
                nuevo.posVertical = pos

                # asignar abajo y arriba para el nodo nuevo
                nuevo.abajo = tmp.abajo
                nuevo.arriba = tmp
                
                tmp.abajo.arriba = nuevo # reasignar arriba para el nodo de abajo
                tmp.abajo = nuevo # reasignar abajo para el nodo actual
                return tmp.abajo

            # pasar al siguiente nodo abajo si no hubo un return
            tmp = tmp.abajo

    def crearIndiceHorizontal(self, pos):
        # recorrer todos los nodos de manera horizontal
        tmp = self.raiz
        while tmp != None:
            # no existe el indice; solo hay índices menores
            if tmp.derecha == None and tmp.posHorizontal < pos:
                # ya no hay más nodos en horizontal
                # se inserta al final
                nuevo = Nodo()
                nuevo.posHorizontal = pos
                nuevo.posVertical = 0
                nuevo.izquierda = tmp
                tmp.derecha = nuevo
                return tmp.derecha
            
            # indice actual es igual a el nuevo índice
            if tmp.posHorizontal == pos :
                # no hacer nada
                return tmp

            # indice actual es menor, pero el siguiente es mayor
            if tmp.posHorizontal < pos and tmp.derecha.posHorizontal > pos:
                # insertar un nodo en medio del nodo actual y del nodo siguiente
                nuevo = Nodo()
                nuevo.posHorizontal = pos
                nuevo.posVertical = 0

                # asignar derecha y arriba para el nodo nuevo
                nuevo.derecha = tmp.derecha
                nuevo.izquierda = tmp
                
                tmp.derecha.izquierda = nuevo # reasignar arriba para el nodo de derecha
                tmp.derecha = nuevo # reasignar derecha para el nodo actual
                return tmp.derecha
                
            # pasar al siguiente nodo derecha si es que no hubo return 
            tmp = tmp.derecha

    def insertarVertical(self, nodo, indiceHorizontal):
        # recorrer todos los nodos de manera horizontal para insertar los verticales
        tmp = indiceHorizontal
        while tmp != None:
            # no existe el indice; solo hay índices menores
            if tmp.abajo == None and tmp.posVertical < nodo.posVertical:
                # ya no hay más nodos en vertical
                # se inserta al final
                nodo.arriba = tmp
                tmp.abajo = nodo
                return tmp.abajo
            
            # indice actual es igual a el nuevo índice
            if tmp.posVertical == nodo.posVertical :
                # no hacer nada, el dato se sobre escribe
                tmp.dato = nodo.dato
                return tmp

            # indice actual es menor, pero el siguiente es mayor
            if tmp.posVertical < nodo.posVertical and tmp.abajo.posVertical > nodo.posVertical:
                # insertar un nodo en medio del nodo actual y del nodo siguiente

                # asignar abajo y arriba para el nodo nuevo
                nodo.abajo = tmp.abajo
                nodo.arriba = tmp
                
                tmp.abajo.arriba = nodo # reasignar arriba para el nodo de abajo
                tmp.abajo = nodo # reasignar abajo para el nodo actual
                return tmp.abajo

            # pasar al siguiente nodo abajo si no hubo return
            tmp = tmp.abajo
       
    def insertarHorizontal(self, nodo, indiceVertical):
        # recorrer todos los nodos en horizontal
        tmp = indiceVertical
        while tmp != None:
            # no existe el indice; solo hay índices menores
            if tmp.derecha == None and tmp.posHorizontal < nodo.posHorizontal:
                # ya no hay más nodos en horizontal
                # se inserta al final
                nodo.izquierda  = tmp
                tmp.derecha = nodo
                return tmp.derecha
            
            # indice actual es igual a el nuevo índice
            if tmp.posHorizontal == nodo.posHorizontal :
                # no hacer nada se sobre escribe
                tmp.dato = nodo.dato
                return tmp

            # indice actual es menor, pero el siguiente es mayor
            if tmp.posHorizontal < nodo.posHorizontal and tmp.derecha.posHorizontal > nodo.posHorizontal:
                # insertar un nodo en medio del nodo actual y del nodo siguiente
                # asignar derecha y arriba para el nodo nuevo
                nodo.derecho = tmp.derecha
                nodo.izquierda = tmp
                
                tmp.derecha.izquierda = nodo # reasignar arriba para el nodo de derecha
                tmp.derecha = nodo # reasignar derecha para el nodo actual
                return tmp.derecha
                
            # pasar al siguiente nodo derecha si esque no hubo return
            tmp = tmp.derecha

    def insertarDato(self,dato,  posVertical, posHorizontal):
        # validar que los índices existan en horizontal y vertical
        indiceVertical = self.crearIndiceVertical(posVertical)
        indiceHorizontal = self.crearIndiceHorizontal(posHorizontal)

        # crear el nodo valor
        nuevo = Nodo()
        nuevo.posHorizontal = posHorizontal
        nuevo.posVertical = posVertical
        nuevo.dato = dato

        # indexar/apuntar nodo nuevo en indice vertical
        nuevo = self.insertarVertical(nuevo, indiceHorizontal) 
        nuevo = self.insertarHorizontal(nuevo, indiceVertical)
        print("Nodo insertado...")
        pass
    
    def recorrerMatriz(self):
        print("Graficando lista...")
        
        dot = Digraph('G', filename='dot', engine='dot',format='svg')
        dot.node_attr.update(shape="box")
        dot.attr(rankdir = "TB")
        contSubgrap = 1
        
        #iniciamos en el nodo raiz
        tmpV = self.raiz

        #vamos bajando en vertical
        while tmpV != None:
            tmpH = tmpV

            #creamos subgrafos para alinearlos            
            c = Digraph('child'+str(contSubgrap))
            c.attr(rank='same')
            contSubgrap += 1

            #nos vamos a la derecha 
            while tmpH != None:
                self.graficarNodos(c, tmpH)
                tmpH = tmpH.derecha

            #se termino una fila, agregamos el subgrafo
            dot.subgraph(c)
            tmpV = tmpV.abajo


        #vuelvo a recorrer para mostrar las flechas
        tmpV = self.raiz
        #vamos bajando en vertical
        while tmpV != None:
            tmpH = tmpV

            #nos vamos a la derecha 
            while tmpH != None:
                self.graficarFlechas(dot, tmpH)
                tmpH = tmpH.derecha

            tmpV = tmpV.abajo
        dot.view()
        pass

    def graficarNodos(self, grafo, nodoE):
        
        nodo = nodoE
        id = str(nodo.posVertical)+"_"+str(nodo.posHorizontal)
        grafo.node(id, nodo.dato,group=str(nodo.posHorizontal))
        

    def graficarFlechas(self, grafo, nodoE):
        nodo = nodoE
        id = str(nodo.posVertical)+"_"+str(nodo.posHorizontal)
        if nodo.posVertical != 0 and nodo.posHorizontal != 0:
            #Graficamos la flecha vertical
            idV1 = nodo.arriba.posVertical
            idV2 = nodo.arriba.posHorizontal
            idV = str(idV1)+"_"+str(idV2)
            grafo.edge(idV, id)
            grafo.edge(id, idV)

            #Ahora graficamos la flecha horizontal
            idH1 = nodo.izquierda.posVertical
            idH2 = nodo.izquierda.posHorizontal
            idH = str(idH1)+"_"+str(idH2)
            grafo.edge(idH,id)
            grafo.edge(id,idH)
        elif nodo.posVertical == 0 and nodo.posHorizontal != 0:
            #es una cabecera horizontal
            idAnterior = str(nodo.izquierda.posVertical)+"_"+str(nodo.izquierda.posHorizontal)
            grafo.edge(idAnterior, id)   
        elif nodo.posHorizontal == 0 and nodo.posVertical != 0:
            #es una cabecera vertical
            idAnterior = str(nodo.arriba.posVertical)+"_"+str(nodo.arriba.posHorizontal)
            grafo.edge(idAnterior, id)
        pass