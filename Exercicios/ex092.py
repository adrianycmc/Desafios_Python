# Desafio 092: Cadastro de trabalhador em Python - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

pessoas = {}

while True:
    nome = str(input("Nome: "))
    ano_nascimento = int(input("Ano de nascimento: "))
    ctps = int(input("Carteira de trabalho (0 não tem): "))
    ano_contratacao = int(input("Ano de contratação: "))
    salario = float(input("Salário: "))

    pessoas = {'nome': nome, 'ano_nascimento': ano_nascimento, 'ctps': ctps, 'ano_contratacao': ano_contratacao, 'salario': salario}
    
    continuar = str(input("Deseja continuar? [S/N]: ")).upper()
    if continuar == 'N':
        break
    
idade = 2025 - pessoas['ano_nascimento']
aposentadoria = pessoas['ano_contratacao'] + 35

print("\n" + "-=" * 30 + "\n")
print(pessoas)
print(f"O campo nome tem o valor {pessoas['nome']}.")
print(f"O campo idade tem o valor {idade}.")
print(f"O campo ctps tem o valor {pessoas['ctps']}.")
print(f"O campo contratação tem o valor {pessoas['ano_contratacao']}.") 
print(f"O campo salário tem o valor R$ {pessoas['salario']:.2f}.")
print(f"O campo aposentadoria tem o valor {aposentadoria}.") 


