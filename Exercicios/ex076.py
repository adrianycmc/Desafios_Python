# Desafio 076: Lista de Preços com Tupla - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular. Uma tupla tem o nome e o preço. O programa deve mostrar o nome e o preço de cada produto, alinhados à direita, com o preço com duas casas decimais e alinhado à esquerda.

lista_precos = (("Almofada", 9.00), ("Tapete", 50.00), ("Cadeira", 150.00), ("Mesa", 250.00), ("Sofá", 500.00))
print("-" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}") # :^40 centraliza o texto.	
print("-" * 40)
for produto in lista_precos:
    print(f"{produto[0]:.<30}R${produto[1]:>7.2f}") 
    #.<30 alinha à esquerda com 30 espaços. >7.2f alinha à direita com 7 espaços e 2 casas decimais.
print("-" * 40)
