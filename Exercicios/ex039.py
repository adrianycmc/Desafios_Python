# Desafio 039: Alistamento Militar - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


ano = int(input('Digite seu ano de nascimento: '))
idade = 2024 - ano

if idade < 18:
    print(f'Você ainda vai se alistar ao serviço militar. Faltam {18 - idade} anos.')
elif idade == 18:
    print('Está na hora de se alistar ao serviço militar.')
else:
    print(f'Já passou do tempo do alistamento. Passaram-se {idade - 18} anos.')