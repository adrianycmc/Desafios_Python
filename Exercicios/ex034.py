# Desafio 034: Aumentos múltiplos - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario_funcionario = float(input('Qual é o seu salário atual? '))
aumento_10 = salario_funcionario + (salario_funcionario * 0.10)
aumento_15 = salario_funcionario + (salario_funcionario * 0.15)

if salario_funcionario > 1250:
    print(f'O seu salário terá um ajusde de 10% e será de: R$ {aumento_10:.2f}')
else:
    print(f'O seu salário terá um ajuste de 15% e será de: R$ {aumento_15:.2f}')