# Desafio 093: Cadastro de Jogador de Futebol - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou e depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}


jogador = str(input("Nome do jogador: "))
partidas = int(input("Quantas partidas ele jogou: "))
gol_partida_1 = int(input(f"Quantos gols ele fez na partida 1: "))
gol_partida_2 = int(input(f"Quantos gols ele fez na partida 2: "))
gol_partida_3 = int(input(f"Quantos gols ele fez na partida 3: "))
gols = [gol_partida_1, gol_partida_2, gol_partida_3]
total = gol_partida_1 + gol_partida_2 + gol_partida_3
    
jogador = {'nome': jogador, 'partidas': partidas, 'gols': gols, 'total': total}
gols_das_partidas = { 'gol_partida_1': gol_partida_1, 'gol_partida_2': gol_partida_2, 'gol_partida_3': gol_partida_3}

        
print("\n" + "-=" * 30 + "\n")
print(jogador)
print("\n" + "-=" * 30 + "\n")
print(f"O campo nome tem o valor {jogador['nome']}.")
print(f"O campo gols tem o valor {jogador['gols']}.")
print(f"O campo total tem o valor {jogador['total']}.")
print("\n" + "-=" * 30 + "\n")
print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")
print(f"=> Na partida 1, fez {gols_das_partidas['gol_partida_1']} gols.")
print(f"=> Na partida 2, fez {gols_das_partidas['gol_partida_2']} gols.")
print(f"=> Na partida 3, fez {gols_das_partidas['gol_partida_3']} gols.")
print(f"Foi um total de {jogador['total']} gols.")