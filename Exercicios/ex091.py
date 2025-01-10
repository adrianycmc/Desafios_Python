# Desafio 091: Jogo de Dados em Python - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. Usar o randint para gerar números aleatórios e guardar no dicionário, o itemgetter para ordenar o dicionário e o sleep para dar um delay na impressão dos resultados.


from random import randint
from time import sleep
from operator import itemgetter

jogos = {}
valor_min_dado = 1
valor_max_dado = 6

for jogador in range(1, 5):
    jogos[f"jogador {jogador}"] = randint(valor_min_dado, valor_max_dado) 
    print(f"O jogador {jogador} tirou {jogos[f'jogador {jogador}']} no dado.")
    sleep(1)
    
    # O jogador é incluído no dicionário com o valor do dado tirado. jogador_{jogador} = jogador_1, jogador_2, jogador_3, jogador_4.
print("-=" * 30)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print("Ranking dos jogadores:")
for ordem, (jogador, valor) in enumerate(ranking):
    print(f"{ordem + 1}º lugar: {jogador} com {valor}.")
    
# itemgetter(1) ordena o dicionário pelo valor, reverse=True ordena do maior para o menor.
# enumerate(ranking) cria uma tupla com o índice e o valor do ranking. ordem é o índice e jogador é o valor.

    
    