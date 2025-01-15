# Desafio 096: Função que calcula área - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def linha():
    print("-=" * 30)

def area(largura, comprimento):
    largura * comprimento
    print(f"A área de um terreno de {largura} x {comprimento} é de {largura * comprimento} m².")

linha()
print("Controle de terrenos".center(60))
linha()

largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area(largura, comprimento)