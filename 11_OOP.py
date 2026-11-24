class Carro :
    # Metodo dunder : Double Underscore Method
    # Metodos especiais e restritos
    def __init__ (self, modelo, cor) :
        self.Modelo     = modelo
        self.cor        = cor
        self.velocidade = 0
    
    def acelerar(self, incremento) :
        self.velocidade += incremento
        print(f'O carro {self.Modelo} acelerou para {self.velocidade}Km/h')
        
    def parar(self) :
        self.velocidade = 0
        print(f'O carro {self.Modelo} parou')
        
    def desacelerar (self) :
        while self.velocidade > 0:
            self.velocidade = max(0, self.velocidade - 5)



# Criando um objeto: O Carro!
carroInstrutor  = Carro ("Jetta GLI", "Preto")
carroLucas      = Carro ("T-Cross","Preto")
carroRafael     = Carro ("Saveiro", "Branco")

carroInstrutor.acelerar(60)
carroInstrutor.acelerar(10)
