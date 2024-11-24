# Desafio 012: Calculando descontos - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input('Digite o preço do produto: R$ '))
preco_produto_desconto = preco_produto - (preco_produto * 0.05)

print(f'O preço do produto com 5% de desconto é R$ {preco_produto_desconto:.2f}.')