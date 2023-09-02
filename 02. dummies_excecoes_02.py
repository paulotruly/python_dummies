while True: 

    try: 
        valor1 = int(input("Digite o primeiro número: "))
        valor2 = int(input("Digite o segundo número: "))
    
        divisao = valor1 / valor2

    except ValueError: 
        print("Você deveria ter digitado um número!")
    except KeyboardInterrupt:
        print("Você apertou Ctrl+C!") 
    except ZeroDivisionError:
        print("Impossível dividir por zero!")
    except ArithmeticError:
        print("Ocorreu um erro no cálculo!")
    
    else:
        print(divisao)

    if input("Deseja digitar outro número? S/N").upper() == 'S':
        pass
    else: 
        break
       