# Desafio 036: Aprovando Empréstimo - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# Calcue o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


valor_casa = float(input('Qual é o valor do imóvel? R$ '))
salario = float(input('Qual é o valor do seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = valor_casa / (anos * 12)
regra_emprestimo = salario * 0.3

if prestacao <= regra_emprestimo:
    print(f'Empréstimo aprovado! O valor mensal da sua prestação será de R$ {prestacao:.2f}')
else:
    print(f'Empréstimo negado! O valor mensal da sua prestação excede 30% do seu salário.')
    
