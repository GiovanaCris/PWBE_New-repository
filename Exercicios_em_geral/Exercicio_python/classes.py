class Cachorro:
    def __init__(self, nome, raca, cor, idade):
        #Atributos
        self.nome = nome
        self.raca_cachorro = raca
        self.cor = cor
        self.idade = idade
        self.orelhas = 2

    #Métodos
    def latir(self):
        print ("au au")

    def correr(self, kms):
        print(f"{self.nome} correu {self.idade} km")

cachorro_da_Lu = Cachorro("Pituco", "Vira-lata", "Caramelo", 15)

cachorro_da_Lu.correr(35)









