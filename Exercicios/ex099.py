# Desafio 099: Função que descobre o maior - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def linha():
    print("-=" * 30)

def maior(lista):
    # for valor in lista:
    #     print(valor, end =' ') 
        print(f"{', '.join(map(str, lista))}. \nForam passados {len(lista)} valores ao todo.")
        print(f"O maior valor informado foi {max(lista)}.")

valores = [7, 2, 5, 0, 4]

linha()
print("Análise dos valores passados...".center(60))
linha()
maior(valores)