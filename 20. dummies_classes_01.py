# Trabalhando com métodos 

class MinhaClasse1: 
    def DigaOlá():
        print("Olá!")

MinhaClasse1.DigaOlá()

# Criando métodos de instância

class MinhaClasse2: 
    def DigaOlá(self):
        print("Olá!")

MinhaInstância1 = MinhaClasse2()
MinhaInstância1.DigaOlá()

# Trabalhando com construtores

class MinhaClasse3:
    Greeting = ""
    
    def __init__(self, Name="there"):
        self.Greeting = Name + "!"
        
    def SayHello(self):
        print("Hello {0}".format(self.Greeting))

MinhaInstância2 = MinhaClasse3()
MinhaInstância2.SayHello()

MinhaInstância2 = MinhaClasse3("Amy")
MinhaInstância2.SayHello()

MinhaInstância2.Greeting = "Harry!"
MinhaInstância2.SayHello()
