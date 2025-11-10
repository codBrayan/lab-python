nome = input("Digite seu nome: ")
idade =input("Digite sua idade: ")

if nome and idade:
    nomeInvertido = nome[::-1]
    if " "in(nome): temEspaco = "Contém espaços"
    else: temEspaco =  "Não contém espaços"
    quantCaracteres = len(nome)
    print(f'''
Seu nome é {nome}
Seu nome invertido é {nomeInvertido}
Seu nome {temEspaco}
Seu nome contem {quantCaracteres} caracteres\
A primeira letra do seu nome é "{nome[0]}"
A ultima letra do seu nome é "{nome[-1]}"
''')
else:
    print("Você não preencheu um dos campos")
