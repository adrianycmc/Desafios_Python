# Desafio 028: Jogo da adivinhação v.1.0 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = random.randint(0, 5)
num_user = int(input('Digite um número entre 0 e 5: '))

if num == num_user:
    print('Parabéns! Você acertou!')
else:
    print('Que pena! Você errou!')