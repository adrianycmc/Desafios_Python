# Desafio 015: Aluguel de carros - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

quantidade_km = float(input('Quantos km foram percorridos? '))
quantidade_dias = int(input('Por quantos dias o carro foi alugado? '))

diaria = 60
km = 0.15
preco = (quantidade_dias * diaria) + (quantidade_km * km)

print(f'O total a pagar é de R${preco:.2f}.')