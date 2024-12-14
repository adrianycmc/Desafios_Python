# Desafio 063: Sequência de Fibonacci v1.0 - Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci. 
# Exemplo: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input('Quantos termos você quer mostrar? '))
termo_1 = 0
termo_2 = 1
contador = 3

while contador <= n:
    termo_3 = termo_1 + termo_2
    print(f'{termo_3} -> ', end='')
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1
print('Fim')