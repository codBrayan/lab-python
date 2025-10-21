print("Para descobrir seu IMC, por favor insira os seguintes dados:")
nome = input("Nome: ")
peso = float(input("Peso (Ex: 86.0): "))
altura = float(input("Altura (Ex: 1.70): "))
valorIMC = peso / altura ** 2
print(f'\n{nome}, seu IMC é de {valorIMC:.2f}') 

if valorIMC <= 18.5:
    print("Abaixo do peso")
elif valorIMC <= 24.9:
    print("Peso Normal")
elif valorIMC <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")


#Para descobrir seu IMC, por favor insira os seguintes dados:
#Nome: Brayan
#Peso (Ex: 86.0): 72.1    
#Altura (Ex: 1.70): 1.70

#Brayan, seu IMC é de 24.95
#Sobrepeso