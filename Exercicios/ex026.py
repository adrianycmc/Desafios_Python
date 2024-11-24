# Desafio 026: Primeira e última ocorrência de uma string - Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A".
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.

frase = input("Digite uma frase: ")

quantidade_a = frase.count('a')
primeira_posicao_a = frase.find('a')
ultima_posicao_a = frase.rfind('a')

print(f'Quantidade de letras "A": {quantidade_a}')
print(f'Primeira posição da letra "A": {primeira_posicao_a}')
print(f'Última posição da letra "A": {ultima_posicao_a}')

# A função count() retorna o número de ocorrências de uma substring em uma string. A função find() retorna a posição da primeira ocorrência de uma substring em uma string. A função rfind() retorna a posição da última ocorrência de uma substring em uma string.