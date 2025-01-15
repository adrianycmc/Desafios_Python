# Desafio 100: Funções para sortear e somar - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.


import random

valores = []

def sorteia():
    print("Sorteando 5 valores da lista: ", end='')
    for contador in range(5):
        valores.append(random.randint(1, 50))
        print(valores[contador], end=' ')
    print(".")

def somaPar():
    soma_pares = sum(numero for numero in valores if numero % 2 == 0)
    print(f"Somando os valores pares de: {', '.join(map(str, valores))}, temos {soma_pares}.")
    
sorteia()
somaPar()