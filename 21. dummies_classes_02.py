# Criando variavéis de instância

class MyClass:
    def DoAdd(self, Value1=0, Value2= 0):
        Sum = Value1 + Value2
        print("The sum of {0} plus {1} is {2}".format(Value1, Value2, Sum))
    
MyInstance = MyClass()
MyInstance.DoAdd(1, 4)

# Usando métodos com listas de argumentos variavéis

class MyClass2:
    def PrintList1(*args):
        for Count, Item in enumerate(args):
            print("{0}. {1}".format(Count, Item))
    
    def PrintList2(**kwargs):
        for Name, Value in kwargs.items():
            print ("{0} likes{1}".format(Name, Value))
            
MyClass2.PrintList1("Red", "Blue", "Green")
MyClass2.PrintList2(George=" Red", Sue=" Blue", Sarah=" Green")

# Sobrecarregando operadores 

class MyClass3:
    def __init__(self, *args):
        self.Input = args
    def __add__(self, Other):
        Output = MyClass3()
        Output.Input = self.Input + Other.Input
        return Output
    def __str__(self):
        Output = ""
        for Item in self.Input:
            Output += Item
            Output += " "
        return Output

Value3 = MyClass3("Red", "Blue", "Green")
Value4 = MyClass3("Yellow", "Purple", "Cyan")
Value5 = Value3 + Value4
print("{0} + {1} = {2}".format(Value3, Value4, Value5))