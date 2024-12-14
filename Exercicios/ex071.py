# Desafio 071: Simulador de Caixa Eletrônico - Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print('{:^30}'.format('BANCÃO DO PYTHICO'))
print('=' * 30 + '\n')

saque = int(input('Quanto você deseja sacar? R$ '))
total = saque
cedula = 50 # A primeira cédula é de R$50.
total_cedula = 0

while True:
    if total >= cedula:      # Se o total for maior ou igual a cédula.
        total -= cedula      # Subtrai o valor da cédula do total.
        total_cedula += 1    # Adiciona 1 ao total de cédulas.
    else:
        if total_cedula > 0:  # Se o total de cédulas for maior que 0.
            print(f'Total de {total_cedula} cédulas de R$ {cedula}.')
        if cedula == 50:    # Se a cédula for de R$50.
            cedula = 20     # A próxima cédula é de R$20.
        elif cedula == 20:  # Se a cédula for de R$20.
            cedula = 10     # A próxima cédula é de R$10.
        elif cedula == 10:  # Se a cédula for de R$10.
            cedula = 1      # A próxima cédula é de R$1.
        total_cedula = 0    # Zera o total de cédulas.
        if total == 0:
            break

print('\n' + '=' * 30 + '\n')
print('Volte sempre ao BANCÃO DO PYTHICO! Tenha um bom dia! \n')
