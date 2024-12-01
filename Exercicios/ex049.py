# Desafio 049: Tabuada v.2.0 - Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número para ver sua tabuada: '))

for tabuada in range(1, 11):
    print(f'{num} x {tabuada} = {num * tabuada}')