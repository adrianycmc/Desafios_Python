# Desafio 10: Conversor de moedas. - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27.

carteira = float(input('Quanto dinheiro você tem na sua carteira? R$ '))
dolar = 3.27
dolar_comprado = carteira / dolar

if carteira >= 3.27:
    print(f'Com R$ {carteira:.2f} você pode comprar US$ {dolar_comprado:.2f}.')   
else:
    print(f'Com R$ {carteira:.2f} você não pode comprar dólares.')