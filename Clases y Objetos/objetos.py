#Declarar la clase
class Espada:
    def __init__(self, material):
        self.material = material

    def Dañar(self):
        print("Te he hecho daño con la espada de: "+self.material)


#Crear instancias de la clase
espadaDiamante = Espada("Diamante")
espadaDiamante.Dañar()

espadaMadera = Espada("Madera")
espadaMadera.Dañar()

espadaHierro = Espada("Hierro")
espadaHierro.Dañar()

miVariable = espadaDiamante.material
print("miVariable es: "+miVariable)