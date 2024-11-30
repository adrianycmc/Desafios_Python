# Desafio 044: Gerenciador de Pagamentos - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros no valor total

preco_produto = float(input('Qual é o preço do produto? R$ '))
pagamento = int(input(''' Qual será a condição de pagamento?
                      1 - À vista dinheiro/cheque.
                      2 - À vista no cartão.
                      3 - Em até 2x no cartão.
                      4 - Em 3x ou mais no cartão.
                      '''))	

vista_dinheiro = preco_produto - (preco_produto * 0.10)
vista_cartao = preco_produto - (preco_produto * 0.05)
parcelado_2x = preco_produto
parcelado_3x = preco_produto + (preco_produto * 0.20)

if pagamento == 1:
    print(f'O valor a ser pago à vista no dinheiro/cheque é de R$ {vista_dinheiro:.2f}.')
elif pagamento == 2:
    print(f'O valor a ser pago à vista no cartão é de R$ {vista_cartao:.2f}.')
elif pagamento == 3:
    print(f'O valor a ser pago em até 2x no cartão é de R$ {parcelado_2x:.2f}. Cada parcela será de R$ {parcelado_2x / 2:.2f}.')
else:
    parcelas = int(input('Quantas parcelas? '))
    print(f'O valor a ser pago em {parcelas}x no cartão é de R$ {parcelado_3x:.2f}. Cada parcela será de R$ {parcelado_3x / parcelas:.2f}.')