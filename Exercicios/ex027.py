# Desafio 027: Primeiro e último nome de uma pessoa - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome_completo = input("Digite seu nome completo: ").split()

primeiro_nome = nome_completo[0]
ultimo_nome = nome_completo[-1]

print(f'O primeiro nome é {primeiro_nome}.')
print(f'O último nome é {ultimo_nome}.')