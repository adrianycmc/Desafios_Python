# Desafio 094: Unindo dicionários e listas - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas; B) A média de idade do grupo; C) Uma lista com todos os valores; D) Uma lista com todas as pessoas com idade acima da média. 

pessoa = {}
pessoas = []
mulheres = []
quantidade_pessoas = 0 

while True:
    nome = str(input("Nome: "))
    while True:
        sexo = str(input("Sexo: ")).upper()
        if sexo == 'M' or sexo == 'F':
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    idade = int(input("Idade: "))
    
    pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}
    pessoas.append(pessoa)
    quantidade_pessoas += 1
    
    while True:
        continuar = str(input("Quer continuar? [S/N] ")).upper()
        if continuar == 'S' or continuar == 'N':
            break
        print("ERRO! Responda apenas S ou N.")
     
    if continuar == 'N':
        break
    
soma_idades = sum(pessoa['idade'] for pessoa in pessoas)
media_idade = soma_idades / quantidade_pessoas

if sexo == 'F':
    mulheres.append(nome)

    
print("\n" + "-=" * 30 + "\n")

print(f"- O grupo tem {quantidade_pessoas} pessoas.")
print(f"- A média de idade é de {media_idade:5.2f} anos.")
print(f"- As mulheres cadastradas foram: {', '.join(mulheres)}.")
print("- Lista de pessoas que estão acima da média: ")
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        print(f"{pessoa['nome']} com {pessoa['idade']} anos.")

print("\n")
        
for pessoa in pessoas:
    print(f"nome = {pessoa['nome']} | sexo = {pessoa['sexo']} | idade = {pessoa['idade']}")
