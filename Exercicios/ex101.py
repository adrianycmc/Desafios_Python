# Desafio 101: Funções para votação - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições. Para resolver esse exercício, pesquise sobre a função date da biblioteca datetime. 


def voto(ano):
    from datetime import date
    idade = date.today().year - ano

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    
print("-----------------------------------")
ano_nascimento = int(input("Em que ano você nasceu? "))
print(voto(ano_nascimento))
    
    