class Person:

    test = 'xuxu'
    def __init__(self,nome,sobrenome,nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento

    def mostrarNome(self):
        print(f'Meu nome é {self.nome}')

    def mostrarSobrenome(self):
        print(f'Meu sobrenome é {self.sobrenome}')

    def mostrarNascimento(self):
        print(f'Meu nascimento foi em {self.nascimento}')

    def mostrarTodosOsDados(self):
        print(f'Meu nome completo é {self.nome} {self.sobrenome} nascido na data de {self.nascimento}')


x = Person.test ##Accessando variavel dentro da classe
print(x)
x = Person('Joao','Skonienczwy','29/09/1984')
x.mostrarNome()
x.mostrarSobrenome()
x.mostrarNascimento()
x.mostrarTodosOsDados()