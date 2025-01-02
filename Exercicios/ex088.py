# Desafio 088: Palpites para a Mega Sena - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. Não pode repetir números em um mesmo jogo. Incluir um timer() para exibir o jogo no console.

import random
from time import sleep

print("-=" * 30)
print("JOGO DA MEGA SENA".center(60))
print("-=" * 30)

jogos = int(input("Quantos jogos você quer que eu sorteie? "))
intervalo_min = 1
intervalo_max = 60

for contador in range(0, jogos):
    jogo = []
    while len(jogo) < 6:
        num = random.randint(intervalo_min, intervalo_max)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    print(f"Jogo {contador + 1}: {jogo}")
    sleep(1)
    