# Desafio 069: Análise de dados do grupo - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) Quantas pessoas tem mais de 18 anos. B) Quantos homens foram cadastrados. C) Quantas mulheres que tem menos de 20 anos.

idade_lista = []
sexo_lista = []

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    
    while sexo not in ['M', 'F']:
        print('Sexo inválido. Digite novamente!')
        sexo = str(input('Digite o sexo [M/F]: ')).upper()

    # Armazenando na lista
    idade_lista.append(idade)
    sexo_lista.append(sexo)
        
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    while continuar not in ['S', 'N']:
        print('Opção inválida. Digite novamente!')    
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()
        
    if continuar == 'N':
        break
    
#  A) Quantas pessoas tem mais de 18 anos.
pessoas_maior_18 = 0
for idade in idade_lista:
    if idade > 18:
        pessoas_maior_18 += 1

print(f'{pessoas_maior_18} pessoas tem mais de 18 anos.')   

# B) Quantos homens foram cadastrados. 
for sexo in sexo_lista:
    homens = sexo_lista.count('M')
print(f'{homens} homens foram cadastrados.')

# C) Quantas mulheres que tem menos de 20 anos.
mulheres_menos_20 = 0
for idade, sexo in zip(idade_lista, sexo_lista):
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
print(f'{mulheres_menos_20} mulheres têm menos de 20 anos.')
