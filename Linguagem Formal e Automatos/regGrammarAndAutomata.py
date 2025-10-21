import re

# Simulação de um Autômato Finito Determinístico (DFA) 

def simula_automato(palavra: str) -> bool:
    """Simula o DFA para a linguagem ab+c."""
    estados = {'q0', 'q1', 'q2', 'q_erro'}
    alfabeto = {'a', 'b', 'c'}
    estado_inicial = 'q0'
    estados_finais = {'q2'}

    # Dicionário representa a função de transição
    transicoes = {
        'q0': {'a': 'q1'},
        'q1': {'b': 'q1', 'c': 'q2'}
    }

    estado_atual = estado_inicial

    for simbolo in palavra:
        if simbolo not in alfabeto:
            estado_atual = 'q_erro'
            break
        
        # Pega o próximo estado do dicionário de transições.
        # Se a transição não existir, vai para o estado de erro.
        estado_atual = transicoes.get(estado_atual, {}).get(simbolo, 'q_erro')

        if estado_atual == 'q_erro':
            break

    # A palavra é aceita se, ao final, o estado atual for um dos estados finais.
    return estado_atual in estados_finais

# Usando as mesmas strings de teste
strings_de_teste = ["abc", "abbc", "abbbbc", "ac", "abb"]

for s in strings_de_teste:
    if simula_automato(s):
        print(f'"{s}" foi aceita pelo autômato.')
    else:
        print(f'"{s}" NÃO foi aceita pelo autômato.')
