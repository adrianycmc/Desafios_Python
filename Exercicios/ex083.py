# Desafio 083: Validando expressões matemáticas - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input("Digite a expressão: "))
pilha_de_parenteses = [] # Lista que simula a pilha de parenteses

for simbolo in expressao:
    if simbolo == "(": 
        pilha_de_parenteses.append("(") 
    elif simbolo == ")": 
        if len(pilha_de_parenteses) > 0: 
            pilha_de_parenteses.pop() 
        else:
            pilha_de_parenteses.append(")") 
            break 
if len(pilha_de_parenteses) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está inválida!")
    
# Explicação: O programa lê uma expressão matemática e verifica se os parênteses estão corretos. Para isso, ele cria uma lista chamada pilha_de_parenteses que simula uma pilha de parenteses. Em seguida, ele percorre a expressão e, se encontrar um parênteses aberto, ele adiciona na pilha. Se encontrar um parênteses fechado, ele verifica se a pilha não está vazia. Se não estiver, ele remove o parênteses da pilha. Caso contrário, ele adiciona o parênteses na pilha e encerra o programa. Por fim, ele verifica se a pilha está vazia. Se estiver, a expressão está válida. Caso contrário, a expressão está inválida.
    