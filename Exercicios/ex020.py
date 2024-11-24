# Desafio 020: Sorteando uma ordem na lista - O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos)

print('A ordem de apresentação dos trabalhos será: ')
for i, aluno in enumerate(alunos, start=1):
    print(f'{i}º lugar: {aluno}')

# random.shuffle() é uma função que embaralha os elementos de uma lista. Nesse caso, a lista alunos foi embaralhada e a ordem dos alunos foi sorteada. A função random.shuffle() modifica a lista original, então não é necessário atribuir o resultado a uma variável.

# for i, aluno in enumerate(alunos, start=1): é um laço de repetição que percorre a lista alunos e imprime a ordem de apresentação dos alunos. A função enumerate() retorna uma tupla com o índice e o elemento da lista. O argumento start=1 indica que o índice começa em 1.
