# Dicionários

Colors = {" Sam": "Blue", " Amy": "Red", " Sarah": "Yellow"}

print(Colors)
print(Colors[" Sam"])
print(Colors.keys())

for Item in Colors.keys():
    print("{0} likes the color {1}!".format(Item, Colors[Item]))
    
Colors[" Sarah"] = "Purple"
print(Colors[" Sarah"])

Colors.update({" Harry": "Orange"})
print(Colors)

for name, color in Colors.items():
    print("{0} likes the color {1}".format(name, color))
    
del Colors[" Sam"]
print(Colors)

print(len(Colors))

Colors.clear()
print(Colors)
print(len(Colors))


