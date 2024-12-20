# Desafio 074: Maior e menor valores em Tupla - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

numeros = ()

# Adicionando números aleatórios à tupla
for n in range(5):
    numeros += (random.randint(1, 10),)
print(f"\nOs números sorteados foram: {numeros}.")

menor_numero = min(numeros)
print(f"O menor número sorteado foi: {menor_numero}.")

maior_numero = max(numeros)
print(f"O maior número sorteado foi: {maior_numero}.")