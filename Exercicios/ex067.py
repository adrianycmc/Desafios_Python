# Desafio 067: Tabuada v3.0 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

num = 0

while True:
    num = int(input('Digite um número para ver a sua tabuada: '))
    if num > -1:
        for tabuada in range(1, 11):
            print(f'{num} x {tabuada} = {num * tabuada}')
    else:
        break
print('Não aceitamos números negativos. Encerrando o programa...')