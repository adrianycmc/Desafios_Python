# Desafio 097: Um print especial - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


def mensagem(texto):
    print("~" * len(texto))
    print(f"{texto}")
    print("~" * len(texto))
    
mensagem("O curso mais legal de Python é o do Guanabara!")