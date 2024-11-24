# Desafio 013: Reajuste salarial - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o seu salário: R$ '))
salario_novo = salario + (salario * 0.15)
print(f'O seu novo salário, com 15% de aumento, é de R$ {salario_novo:.2f}.')