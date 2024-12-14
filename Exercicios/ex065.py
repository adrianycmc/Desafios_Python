# Desafio 065: Maior e menor valores - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

total = 0
contador = 0
numeros = []    # Lista vazia para armazenar os números digitados.

while True:
    num = int(input('Digite um número (Digite 0 para parar): '))
    if num == 0:
        break
    numeros.append(num)    # Adiciona o número digitado à lista.
    total = num + total    # Soma os números digitados.
    contador += 1    # Contador para saber quantos números foram digitados.
    
    # print('---' * 10)
    # print(f'\n Quantas vezes números foram digitados: {contador} \n Total de números digitados: {total} \n')
    # print('---' * 10)
    
if numeros:
    maior = max(numeros)   # Função max() para encontrar o maior valor da lista.
    menor = min(numeros)   # Função min() para encontrar o menor valor da lista.
    media = total / contador
    print(f'O maior valor digitado foi {maior} e o menor valor digitado foi {menor}.')
    print(f'A média dos números digitados foi {media}.')
else:
    print('Nenhum número foi digitado.')
    
