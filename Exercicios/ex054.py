# Desafio 054: Grupo de Maioridade - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. Considerar a maioridade a partir de 21 anos.

from datetime import date

ano_atual = date.today().year
maoioridade = 0
menoridade = 0


for pessoa in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {pessoa}ª pessoa: '))
    idade = ano_atual - nascimento # Calcula a idade da primeira pessoa
    if idade >= 21:
        maoioridade += 1
    else:
        menoridade += 1

print(f'{maoioridade} pessoas são maiores de idade.')
print(f'{menoridade} pessoas são menores de idade.')
