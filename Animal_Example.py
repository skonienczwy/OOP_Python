class Animal:
    def __init__(self,name,family,origin):
        self.name = name
        self.family = family
        self.origin = origin


    def nameOfAnimal(self):
        print(f'É um/uma {self.name}')

    def kindOfAnimal(self):
        print(f'É um/uma {self.family}')

    def originOfAnimal(self):
        print(f'O {self.name} é originario do {self.origin}')


x = Animal('Tucano','Ave','Brasil')
x.nameOfAnimal()
x.kindOfAnimal()
x.originOfAnimal()

