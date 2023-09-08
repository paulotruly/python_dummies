List1 = ["One", 1, "Two", "Three"]
print(List1)

List2 = [0, 1, 2, 3, 4, 5]
for Item in List2:
    print(Item)
    
Colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
ColorSelect = ""

while str.upper(ColorSelect) != "QUIT":
    ColorSelect = input("Please type a color name: ")
    if (Colors.count(ColorSelect) >= 1):
        print("The color exists in the list!")
    elif (str.upper(ColorSelect) != "QUIT"):
        print("The list doesn't contain the color!")
        
