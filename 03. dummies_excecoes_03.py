tentardnv = True

while True: 
    
    try: 
        valor = int(input("Digite um número inteiro: "))
        
    except ValueError: 
        print("Você deveria ter digitado um valor inteiro!")
    
    except KeyboardInterrupt:
        print("Você digitou Ctrl+C!")
        print("Até a próxima!")
           
    else:
        print(valor)
    
    if input("Deseja digitar outro número? S/N").upper() == 'S':
        pass
    else: 
        break
            