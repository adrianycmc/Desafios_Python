# Desafio 037: Conversor de Bases Numéricas - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
      1 - Convertar para Binário
      2 - Convertar para Octal
      3 - Convertar para Hexadecimal
      ''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} convertido para binário é igual a {bin(num)[2:]}.')
elif opcao == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}.')
elif opcao == 3:
    print(f'{num} convertido para Hexadecimal é igual a {hex(num)[2:]}.')
else:
    print('Opção inválida!')


