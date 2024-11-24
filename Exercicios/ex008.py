# Desafio 008: Conversor de medidas. - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor_metros = float(input('Digite um valor em metros: '))
valor_centimetros = valor_metros * 100
valor_milimetros = valor_metros * 1000

print(f'{valor_metros} metros equivalem a {valor_centimetros} centímetros e {valor_milimetros} milímetros.')