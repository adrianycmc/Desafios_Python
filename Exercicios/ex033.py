# Desafio 033: Maior e menor valores - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numeros_str = input('Digite três números separados por espaço: ').split()

numeros_int = [int(numero) for numero in numeros_str]

maior_numero = max(numeros_int)
menor_numero = min(numeros_int)

print(f'O maior número é {maior_numero} e o menor número é {menor_numero}.')