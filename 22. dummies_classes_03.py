# Construindo uma classe-mãe e uma classe-filha

class Animal:
    
    def __init__(self, Nome="", Idade=0, Tipo=""):
        self.Nome = Nome
        self.Idade = Idade
        self.Tipo = Tipo
        
    def GetNome(self):
        return self.Nome
    def SetNome(self, Nome):
        self.Nome = Nome
    def GetIdade(self):
        return self.Idade
    def SetIdade(self, Idade):
        self.Idade = Idade
    def GetTipo(self):
        return self.Tipo
    def SetTipo(self, Tipo):
        self.Tipo = Tipo
    
    def __str__(self):
        return "{0} é uma {1} com {2} anos".format(self.Nome, self.Tipo, self.Idade)
    
    
class Galinha(Animal):
    
    def __init__(self, Nome="", Idade=0):
        self.Nome = Nome
        self.Idade = Idade
        self.Tipo = "Galinha"
    
    def SetTipo(self, Tipo):
        print("Desculpe, {0} sempre será um {1}".format(self.Nome, self.Tipo))
    def Som(self):
        print("{0} diz: có, có, có, có!".format(self.Nome))
        

MinhaGalinha = Galinha("Sally", 2)
print(MinhaGalinha)
MinhaGalinha.SetIdade(MinhaGalinha.GetIdade() + 1)
print(MinhaGalinha)
MinhaGalinha.SetTipo("Gorila")
print(MinhaGalinha)
MinhaGalinha.Som()