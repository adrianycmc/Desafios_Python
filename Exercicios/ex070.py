# Desafio 070: Estatísticas em produtos - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A) Qual é o total gasto na compra. B) Quantos produtos custam mais de R$ 1000. C) Qual é o nome do produto mais barato.

produto_lista = []
preco_lista = []

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$ '))
    
    # Armazenando na lista
    produto_lista.append(produto)
    preco_lista.append(preco)
    
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    while continuar not in ['S', 'N']:
        print('Opção inválida. Digite novamente!')
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()
        
    if continuar == 'N':
        break

print('\n' + '=' * 30 + '\n')    
# A) Qual é o total gasto na compra.
total_compta = sum(preco_lista)
print(f'O total gasto na compra foi R$ {total_compta:.2f}.')

# B) Quantos produtos custam mais de R$ 1000.
produtos_mais_1000 = 0
for preco in preco_lista:
    if preco > 1000:
        produtos_mais_1000 += 1    
print(f'{produtos_mais_1000} produtos custam mais de R$ 1000.')

# C) Qual é o nome do produto mais barato.
if produto_lista and preco_lista:
    produto_mais_barato = produto_lista[preco_lista.index(min(preco_lista))]
    print(f'O produto mais barato é {produto_mais_barato}.')
else:
    print('Nenhum produto foi cadastrado.')