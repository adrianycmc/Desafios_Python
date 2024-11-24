# Desafio 031: Custo da viagem - Desenvolva um programa que pergunte a distância de uma viagem em km. 
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km e R$0,45 para viagens mais longas.

distancia_viagem = float(input('Qual é a distância da sua viagem em km? '))
viagem_curta = distancia_viagem * 0.50
viagem_longa = distancia_viagem * 0.45

if distancia_viagem <= 200:
    print(f'O preço da sua passagem será: R$ {viagem_curta:.2f}')
else:
    print(f'O preço da sua passagem será: R$ {viagem_longa:.2f}')

