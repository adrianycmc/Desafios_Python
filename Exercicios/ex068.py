# Desafio 068: Jogo do Par ou Ímpar - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

vitorias = 0

while True:
    jogador = int(input('Digite um número:  '))
    numero_jogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    
    computador = random.randint(0, 10)
    
    soma = jogador + computador
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
        
        if numero_jogador == resultado:
            print(f'Você jogou {jogador} e o computador jogou {computador}. A soma deu {soma}. Você venceu!')
            vitorias += 1
        else:
            print(f'Você jogou {jogador} e o computador jogou {computador}. A soma deu {soma}. Você perdeu e sai desse jogo com {vitorias} vitórias.')
            break