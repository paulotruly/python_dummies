Value = input("Typeless than 6 characters: ")
LetterNum = 1

for Letter in Value:
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum +=1
    if LetterNum > 6:
        print("The string is too long!")
        break
else: 
    print("The string it's blank!")