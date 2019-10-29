class Car:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrarCarro(self):
        print(f'A marca do carro é {self.marca} e o modelo é {self.modelo}')



x = Car('Audi','A3')
y = Car('Teste','Teste 2')
x.mostrarCarro()
y.mostrarCarro()
