# Desafio 045: GAME: Pedra, Papel e Tesoura. Crie um programa que faça o computador jogar Jokenpô com você.

import random

user_pessoa = input('Escolha entre Pedra, Papel ou Tesoura: ').capitalize()

jokenpo = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(jokenpo)

print(f'O computador escolheu: {pc}')

if user_pessoa == pc:
    print('Empate!')
elif (user_pessoa == 'Pedra' and pc == 'Tesoura') or (user_pessoa == 'Papel' and pc == 'Pedra') or (user_pessoa == 'Tesoura' and pc == 'Papel'):
    print('Você venceu!')
else:
    print('Você perdeu!')

# random.choice() retorna um elemento aleatório de uma sequência não vazia.