# Desafio 022: Analisador de textos - Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo: ")

print(f'Seu nome em com as letras maiúsculas é: {nome.upper()}.')
print(f'Seu nome com as letras minusculas é: {nome.lower()}.')

print(f'Seu nome tem {len(nome.replace(" " , ""))} letras.')
# O método replace() retorna uma cópia da string na qual o valor especificado é substituído por outro valor. Nesste caso, o método replace() foi utilizado para substituir os espaços em branco por uma string vazia, e o método len() foi utilizado para contar o número de caracteres da string resultante.

nome_dividido = nome.split()
print(f'Seu primeiro nome tem {len(nome_dividido[0])} letras.')