from Estructuras import MatrizOrtogonal 

if __name__ == '__main__':
    matrizOrtogonal = MatrizOrtogonal()
    matrizOrtogonal.insertarDato("juan.1-1",1,1)
    matrizOrtogonal.insertarDato("juan.5-5",5,5)
    matrizOrtogonal.insertarDato("juan.3-3",3,3)
    matrizOrtogonal.insertarDato("juan.10-10",10,10)
    matrizOrtogonal.insertarDato("juan.1-13",1,13)
    matrizOrtogonal.insertarDato("juan.2-2",2,2)
    matrizOrtogonal.insertarDato("juan.2-3",2,3)
    matrizOrtogonal.insertarDato("juan.2-13",2,13)
    matrizOrtogonal.insertarDato("juan.5-4",5,4)
    matrizOrtogonal.insertarDato("juan.4-5",4,5)
    matrizOrtogonal.insertarDato("juan.1-2",1,2)
    matrizOrtogonal.insertarDato("juan.2-2",1,3)
    matrizOrtogonal.insertarDato("juan.2-2",1,4)
    
    matrizOrtogonal.recorrerMatriz()