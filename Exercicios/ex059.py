# Desafio 059: Criando um menu de opções - Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, [ 4 ] novos números, [ 5 ] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))

print('''
      Menu do programa:
      
      [1] Somar
      [2] Multiplicar
      [3] Maior
      [4] Novos Números
      [5] Sair do programa
      ''')

opcao = 0
while opcao != 5:
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        print(f'Você escolheu a opção 1 - Somar: {num_1} + {num_2} = {num_1 + num_2}.')
    elif opcao == 2:
        print(f'Você escolheu a opção 2 - Multiplicar: {num_1} x {num_2} = {num_1 * num_2}.')
    elif opcao == 3:
        print(f'Você escolheu a opção 3 - Maior: {max(num_1, num_2)}.')
    elif opcao == 4:
        print('Você escolheu a opção 4 - Digite os números novamente.')
        num_1 = int(input('Digite o primeiro número novamente: '))
        num_2 = int(input('Digite o segundo número novamente: '))        
    elif opcao == 5:
        print('Você escolheu a opção 5 - Sair do programa.')
        break