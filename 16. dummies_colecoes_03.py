# Substituindo a instrução switch por um dicionário

def PrintBlue():
    print("You chose BLUE!\r\n")
def PrintOrange():
    print("You chose ORANGE!\r\n")
def PrintRed():
    print("You chose RED!\r\n")
def PrintYellow():
    print("You chose YELLOW!\r\n")

ColorSelect = {
    0: PrintBlue,
    1: PrintOrange,
    2: PrintRed,
    3: PrintYellow
}

Selection = 0

while (Selection != 4):
    print("0. Blue")
    print("1. Orange")
    print("2. Red")
    print("3. Yellow")
    print("4. Quit!")
    Selection = int(input("Select a color option: "))
    if (Selection >= 0) and (Selection < 4 ):
        ColorSelect[Selection]()