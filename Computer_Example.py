class Computer:
    def __init__(self,processador,memoria,hd,placa_de_video,preco):
        self.processador = processador
        self.memoria = memoria
        self.hd = hd
        self.placa_de_video = placa_de_video
        self.preco = preco

    def mostrarProc(self):
        print(f'Processador : {self.processador}')
    def mostrarMem(self):
        print(f'Memória : {self.memoria} GB')

    def mostrarHd(self):
     print(f'HD com capacidade de : {self.hd} GB')

    def mostrarPlaca(self):
        print(f'Placa de Vídeo: {self.placa_de_video} ')

    def mostrarPreco(self):
        print(f'O preço do computador é de R${self.preco}')





x = Computer('Intel',32,2000,'GTX1080 TI',3090.00)
x.mostrarProc()
x.mostrarMem()
x.mostrarHd()
x.mostrarPlaca()
x.mostrarPreco()

