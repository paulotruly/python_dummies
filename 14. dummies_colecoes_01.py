# Tuplas: coleção usada para criar listas complexas
# nas quais você pode incorporar uma tupla em outra

MyTuple = ("Red", "Blue", "Green")

print(MyTuple)

MyTuple = MyTuple.__add__(("Purple",))

print(MyTuple)

MyTuple = MyTuple.__add__((" Yellow", (" Orange", "Black")))

print(MyTuple)

MyTuple = ("Magenta", ) + MyTuple

print(MyTuple)

print(MyTuple[6])

print(MyTuple[6][0])