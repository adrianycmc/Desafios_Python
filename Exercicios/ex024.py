# Desafio 024: Verificando as primeiras letras de um texto - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input("Digite o nome de uma cidade: ").upper()
primeira_palavra_cidade = cidade.split()[0]

if primeira_palavra_cidade == "SANTO":
    print("O nome da cidade começa com 'SANTO'.")
else:
    print("O nome da cidade não começa com 'SANTO'.")