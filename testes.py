operacao = input("Digite a operação (+, -, *, /): ")
# Verifica se a operação é válida
if operacao not in ('+', '-', '*', '/'):
    print("Operação inválida.") 
else:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: Divisão por zero.")
            else:
                resultado = num1 / num2
        
        if operacao != '/' or num2 != 0:
            print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")