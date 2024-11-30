# Desafio 040: Aquele clássico da Média - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO

nota_1 = float(input('Qual foi sua primeira nota? '))
nota_2 = float(input('Qual foi sua segunda nota? '))

media = (nota_1 + nota_2) / 2

if media < 5.0:
    print(f'Sua média foi {media:.1f}. Você está REPROVADO.')
elif 5.0 <= media <= 6.9:
    print(f'Sua média foi {media:.1f}. Você está de RECUPERAÇÃO.')
else: 
    print(f'Sua média foi {media:.1f}. Você está APROVADO.')