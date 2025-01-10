# Desafio 090: Dicionário em Python - Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.


boletim = {'nome': str(input('Nome: ')), 'média': float(input('Média: '))}

if boletim['média'] >= 7:
    boletim['situação'] = 'Aprovado'
else:
    boletim['situação'] = 'Reprovado'
    
print(f"O nome é igual a {boletim['nome']}. \nA média é igual a {boletim['média']}. \nA situação é igual a {boletim['situação']}.")


