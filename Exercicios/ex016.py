# Desafio 016: Quebrando um número - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

import math

num = float(input('Digite um número:'))
print(f'O número {num} tem a parte inteira {math.trunc(num)}.')

# math.trunc() é uma função que retorna a parte inteira de um número real, ou seja, ele corta a parte decimal do número.