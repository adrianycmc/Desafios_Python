# Desafio 057: Validação de dados - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.


pessoa = str(input('Informe o sexo da pessoa [M/F]: ')).upper()

while pessoa != 'M' and pessoa != 'F':
    pessoa = str(input('Dados inválidos. Por favor, informe o sexo da pessoa [M/F]: ')).upper()
    
print(f'Sexo da pessoa: {pessoa} registrado com sucesso.')