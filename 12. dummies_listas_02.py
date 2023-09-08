Colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
ColorSelect = ""

for Item in Colors:
    print(Item, end=" ")
    
print()
Colors.sort()
for Item in Colors:
    print(Item, end=" ")
    
print()
Colors.reverse()
for Item in Colors:
    print(Item, end=" ")
    
print()
print(*Colors, sep='\n')

print()
for Item in Colors:
    print(Item.rjust(8), sep='\n')
    
print()
print('\n'.join(Colors))

print()
print('First:  {0}\nSecond: {1}'.format(*Colors))