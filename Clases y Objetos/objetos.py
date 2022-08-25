#Declaración de la clase espada
class Espada:
    def __init__(self, material):
        self.material = material

    def Dañar(self):
        print("Daño con la espada de: "+self.material)

#creando instancias
espDiamante = Espada("Diamante")
espDiamante.Dañar()

espHierro = Espada("Hierro")
espHierro.Dañar()

espMadera = Espada("Madera")
espMadera.Dañar()

print(type(espMadera))
