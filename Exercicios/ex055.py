# Desafio 055: Maior e menor da sequência - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# Lista de pesos
pesos = []

for pessoa in range(1,6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    pesos.append(peso) # Adicionando o peso na lista de pesos.
    
# Encontrando o maior e o menor valor na lista:
maior_peso = max(pesos)
menor_peso = min(pesos)

print(f'O maior peso lido foi {maior_peso} kg e o menor peso lido foi {menor_peso} kg.')