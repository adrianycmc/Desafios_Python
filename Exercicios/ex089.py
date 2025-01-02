# Desafio 089: Boletim com listas compostas - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

print("-=" * 30)
print("BOLETIM ESCOLAR".center(60))
print("-=" * 30)

boletim = []

while True: 
    nome = str(input("Nome: "))
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    media = (nota_1 + nota_2) / 2
    print("Aluno cadastrado com sucesso...")
    boletim.append([nome, [nota_1, nota_2], media])
    
    continuar = str(input("Deseja continuar? [S/N]: ")).upper()
    while continuar not in ['S', 'N']:
        print("Opção inválida. Digite novamente!")
        continuar = str(input("Deseja continuar? [S/N]: ")).upper()
    if continuar == 'N':
        break
    
print("\n" + "-=" * 30 + "\n")

print("Boletim".center(60))
for aluno in boletim:
    print(f"Nome: {aluno[0]} - Média: {aluno[2]}")
    
print("\n" + "-=" * 30 + "\n")

while True:
    opcao = str(input("Deseja ver as notas de algum aluno? [S/N]: ")).upper()
    if opcao == "N":
        break
    nome_aluno = str(input("Digite o nome do aluno: "))
    for aluno in boletim:
        if aluno[0] == nome_aluno:
            print(f"Notas de {nome_aluno}: {aluno[1]}")
            break
    else:
        print("Aluno não encontrado.")
