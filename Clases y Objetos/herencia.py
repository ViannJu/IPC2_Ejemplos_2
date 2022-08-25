#Definir clase padre
class Animal:

    __nombre = "Firulais"

    def __init__(self, especie):
        self.especie = especie

    def Hablar(self):
        print("Estoy hablando")

class Perro(Animal):
    def __init__(self, hablar):
        self.hablar = hablar

    def Hablar(self):
        print("Guau")

class Abeja(Animal):
    def __init__(self, hablar):
        self.hablar = hablar
        self.perrito = Perro()

    def Hablar(self):
        print(self.hablar)

    def picar(self):
        print("Te he picado!")

miAbeja = Abeja("Bzzz!")
miAbeja.picar()
miAbeja.Hablar()
print(miAbeja.__nombre)
miAbeja.perrito.hablar

    


