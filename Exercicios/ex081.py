# Desafio 081: Extraindo dados de uma Lista - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

lista_de_valores = []

while True:
    valor = int(input("Digite um valor: "))
    
    if valor not in lista_de_valores:
        lista_de_valores.append(valor) # Adiciona o valor na lista
        print("Valor adicionado com sucesso...")
    else:
        print("Ops valor duplicado! Não vou adicionar...")
        
    continuar = str(input("Deseja continuar? [S/N]: ")).upper()
    while continuar not in ['S', 'N']:
        print("Opção inválida. Digite novamente!")
        continuar = str(input("Deseja continuar? [S/N]: ")).upper()
    if continuar == 'N':
        break
    
# A) Quantos números foram digitados.
print(f"\nVocê digitou {len(lista_de_valores)} elementos em sua lista.")

# B) A lista de valores, ordenada de forma decrescente.
lista_de_valores.sort(reverse=True)
print(f"Os valores digitados em ordem decrescente foram: {lista_de_valores}.")

# C) Se o valor 5 foi digitado e está ou não na lista.

if 5 in lista_de_valores:
    print("O valor 5 foi digitado e está na lista.")
else:
    print("O valor 5 não foi digitado e não está na lista.")