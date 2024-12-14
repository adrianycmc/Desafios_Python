# Desafio 066: Vários números com flag - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = 0
soma = 0
contador_de_numeros = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma = num + soma
    contador_de_numeros += 1
print (f'Foram digitados {contador_de_numeros} e a soma entre eles foi {soma}.')