while True: 

    try: 
        print("1. Ovos")
        print("2. Panquecas")
        print("3. Waffles") 
        print("4. Mingau de aveia")

        MainChoice = int(input("Escolha um item de café da manhã: "))
        
    except ValueError:
        print("Erro! Você deveria ter digitado um número!")
    except KeyboardInterrupt:
        print("Erro! Ctrl+C!")
    except:
        print("Erro!")
    else:

        if (MainChoice == 2):
            Meal = "Panquecas"
        elif (MainChoice == 3):
            Meal = "Waffles"
        if (MainChoice == 1):
            print("1. Pão tostado")
            print("2. Pão fermentado natural")
            print("3. Panquecas")
            Bread = int(input("Escolha um tipo de pão: "))
            if (Bread == 1):
                print("Você escolheu pão tostado acompanhado com ovos!")
            elif (Bread == 2):
                print("Você escolheu pão fermentado natural acompanhado com ovos!")
            elif (Bread == 3):
                print("Você escolheu panquecas acompanhadas com ovos!")
            else: 
                print("Nós temos os ovos, mas sua escolha do pão é inválida!")
        elif (MainChoice == 2 or MainChoice == 3): 
            print("1. Calda doce")
            print("2. Morangos")
            print("3. Açúcar refinada")
            Topping = int(input("Escolha um recheio: "))
            if (Topping == 1):
                print("Você escolheu " + Meal + " recheado com calda doce!")
            elif (Topping == 2):
                print("Você escolheu " + Meal + " recheado com morangos!")
            elif (Topping == 3):
                print("Você escolheu " + Meal + " recheado com açúcar refinada!")
            else: 
                print("Nós temos "+ Meal + " mas sua escolha de recheio é inválida!")
        elif (MainChoice == 4):
            print("Por hoje, só um mingau de aveia!")
        else:
            print("Sinto muito, não servimos esse tipo de café da manhã!")
            
    if input("Tentar pedir novamente? S/N").upper() == 'S':
        pass
    else: 
        break
            