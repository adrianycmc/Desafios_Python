# Desfio 050: Soma de pares - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0 # variavel para somar os numeros pares

for nums in range(1, 13):
    if nums % 2 == 0: # verificando os impares em nums
        soma += nums # se for par soma os numeros
    
print(f'A soma dos pares é {soma}')
        