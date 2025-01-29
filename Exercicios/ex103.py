# Desafio 103: Ficha do Jogador - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome="<desconhecido>", gols=0):
    
    if nome == "":
        nome = "<desconhecido>"
    if gols == "":
        gols = 0
    else:
        gols = int(gols)
          
    return f"O jogador {nome} fez {gols} gol(s) no campeonato."

print("-----------------------------------")
nome = input("Nome do Jogador: ")
gols = input("Gols: ")

print(ficha(nome, gols))