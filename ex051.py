# Desafio 051: Progressão aritmética - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. Exercício que pula de número em número, sem repetir.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro_termo + (10 - 1) * razao

for contagem in range(primeiro_termo, decimo + razao, razao):
    print(contagem, end=' -> ')
print('Fim')