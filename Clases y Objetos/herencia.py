#Definir una clase padre
class Animal:
    def __init__(self, especie):
        self.especie = especie

    def Hablar(self):
        pass

    def Describeme(self):
        print("Soy un animal de tipo: "+type(self).__name__)

#Definir clases hijas
class Perro(Animal):
    def __init__(self, hablar):
        self.hablar = hablar

    def Hablar(self):
        print("Guau!")

class Abeja(Animal):
    def __init__(self, hablar):
        self.hablar = hablar

    def Hablar(self):
        print("Bzzz!")

    def Picar(self):
        print("Te he picado!")

#Declarar instancias
miAbeja = Abeja("Bzzz!")
miAbeja.Hablar()
miAbeja.Picar()
miAbeja.Describeme()