# Desafio 041: Classificando Atletas - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = 2024 - ano_nascimento

if idade <= 9:
    print(f'O atleta tem {idade} anos. Categoria: MIRIM.')
elif 10 <= idade <= 14:
    print(f'O atleta tem {idade} anos. Categoria: INFANTIL.')
elif 15 <= idade <= 19: 
    print(f'O atleta tem {idade} anos. Categoria: JÚNIOR.')
elif idade == 20:
    print(f'O atleta tem {idade} anos. Categoria: SÊNIOR.')
else:
    print(f'O atleta tem {idade} anos. Categoria: MASTER.')