# Desafio 064: Tratando vários valores v1.0 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = 0
soma = 0

while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        soma = num + soma # É iniciada com 0 e a cada interação é somado o valor digitado pelo usuário.
    else:
        break
print(f'A soma dos números foi {soma}')
    