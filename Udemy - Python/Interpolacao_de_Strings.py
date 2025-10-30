#Strings sao iteraveis, ou seja, podemos navegar pelo seus itens. Exemplo:
variavel_1="Brayan"
#print(variavel_1[3]) # y
#print(variavel_1[-3]) #y


#A interpolação de strings no Python permite inserir valores de variáveis e expressões em uma string, exemplo de interpolação é o .format(), f'string' e %f

teste="aaaaaa"
#print("Braya{}n".format(teste))
#print(f'Braya{teste}n')
#print("Braya%sn"%teste)
# Resultado: Brayaaaaaaan

# FOrmatação de strings com fString

# "Completar com 0s até chegar a 15 caract. no total"
variavel = 'SysBiblio'
print(f'{variavel:0>15}')  #000000SysBiblio
print(f'{variavel:0^15}')  #000SysBiblio000

#Format numeros
print(f'{10000.165165:+,.2f}') #+10,000.17
#Exemplo: Printar um numero com 7 digitos mesmo o valor não chegando no millhão
valorDisponivel = 650.25
print(f'Valor Positivo: {valorDisponivel:0=10,}') # Valor Positivo: +0,000,650.25

# Utilizando o fatiamento
variavel = 'Brayan'
print(variavel[::2]) #Percorre meu nome pulando uma casa
print(variavel[::-1]) # Percorre meu nome comecando pela ultima casa

lista = [1 , 2 , 3, 4, 5]
print(lista[::1]) #[1, 2, 3, 4, 5]