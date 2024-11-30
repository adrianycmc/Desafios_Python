# Desafio 038: Comparando Números - Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem: 
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))

if valor_1 > valor_2:
    print('O primeiro valor é maior.')
elif valor_1 < valor_2:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
    