while True: 
    
    try: 
        valor = float(input("Digite um número de 1 a 10: "))
    except ValueError:
        print("O valor informado deve ser um número e estar entre 1 a 10!")
    except KeyboardInterrupt:
        print("Você apertou Ctrl+C!")
    except:
        print("Erro genérico!")
    else:
        if (valor > 0) and (valor <= 10):
            print("Você digitou", valor)
        else: 
            print("O valor informado é inválido!")
            
            
    
    if input("Deseja digitar outro número? S/N").upper() == 'S':
        pass
    else: 
        break