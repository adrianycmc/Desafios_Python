# Desafio 025: Procurando uma string dentro de outra - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Digite seu nome completo: ").upper()

if "SILVA" in nome:
    print("Seu nome tem 'SILVA'.")
else:
    print("Seu nome não tem 'SILVA'.")