# Desafio 029: Radar eletrônico - Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada km acima do limite.

velocidade_carro = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade_carro - 80) * 7

if velocidade_carro > 80:
    print(f'Você foi multado por excesso de velocidade! O valor da sua multa é R$ {multa:.2f}.')
else:
    print('Tenha um bom dia! Dirija com segurança!')