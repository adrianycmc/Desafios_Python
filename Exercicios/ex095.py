# Desafio 095: Aprimorando os Dicionários: Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
jogadores = []

while True:
    jogador = str(input("Nome do jogador: "))
    partidas = int(input("Quantas partidas ele jogou: "))
    total = 0
        
    jogador = {'nome': jogador, 'partidas': partidas, 'total': total, 'gols': []}
    
    gols = []
    for partida in range(partidas):
        gol = int(input(f"Quantos gols ele fez na partida {partida + 1}: "))
        gols.append(gol)
        total += gol
    
    jogador['gols'] = gols
    jogador['total'] = total
    
    jogadores.append(jogador)
    
    continuar = str(input("Deseja continuar? [S/N]: ")).upper()
    if continuar == 'N':
        break
    
    
print("\n" + "-=" * 30 + "\n")
print("\n# cod nome     gols       total")
print("# -----------------------------")
for cod, jogador in enumerate(jogadores):
    print(f"# {cod:<3} {jogador['nome']:<8} {str(jogador['gols']):<10} {jogador['total']}")
    
while True:
    consulta = int(input("Mostre dados de qual jogador? (999 para parar) "))
    if consulta == 999:
        break
    if consulta >= len(jogadores):
        print(f"ERRO! Não existe jogador com código {consulta}! Tente novamente.")
    else:
        jogador = jogadores[consulta]
        print(f"=> Levantamento do jogador {jogador['nome']}: ")
        for partida, gol in enumerate(jogador['gols']):
            print(f"=> No jogo {partida + 1} fez {gol} gols.")
            
