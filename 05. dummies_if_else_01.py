while True: 

    try: 
        print("1. Red")
        print("2. Orange")
        print("3. Yellow")
        print("4. Green")
        print("5. Blue")
        print("6. Purple")
        Choice = int(input("Select your favorite color: "))
    except ValueError:
        print("Error: You must to type a number!")
    except KeyboardInterrupt:
        print("Error: Ctrl+C!")
    except:
        print("Random error!")
    else:
        
        if (Choice == 1):
            print("Your favorite color is RED!")
        elif (Choice == 2):
            print("Your favorite color is ORANGE!")
        elif (Choice == 3):
            print("Your favorite color is YELLOW!")
        elif (Choice == 4):
            print("Your favorite color is GREEN!")
        elif (Choice == 5):
            print("Your favorite color is BLUE!")
        elif (Choice == 6):
            print("Your favorite color is PURPLE!")
        else:
            print("You made a invalid choice!")
        
    if input("Try again? Y/N ").upper() == 'Y':
        pass
    else: 
        break