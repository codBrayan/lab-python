# Sempre precisamos tratar o input do usuário
numeroInput = input = ('Vou dobrar o número que você mandar: ')
try: 
    numero_float = float(numeroInput) #Fail Fast
    print(f'O dobro do número {numeroInput} é {numero_float * 2}')
except:
    print('Isso não é um número')
    