# Desafio 084: Lista composta e análise de dados - Crie um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. (< 100) C) Uma listagem com as pessoas mais leves. (> 70)

pessoas = []


while True:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    pessoas.append([nome, peso])
    print("Pessoa cadastrada com sucesso...")
        
    continuar = str(input("Deseja continuar? [S/N]: ")).upper()
    while continuar not in ['S', 'N']:
        print("Opção inválida. Digite novamente!")
        continuar = str(input("Deseja continuar? [S/N]: ")).upper()
    if continuar == 'N':
            break

print("\n" + "-=" * 30 + "\n")

print(f"Foram cadastradas {len(pessoas)} pessoas.")

pessoa_mais_pesada = None
for pessoa in pessoas:
    if pessoa[1] >= 100:
        if pessoa_mais_pesada is None or pessoa[1] > pessoa_mais_pesada[1]:
            pessoa_mais_pesada = pessoa

if pessoa_mais_pesada:
    print(f"O maior peso foi de {pessoa_mais_pesada[1]}Kg. Peso de {pessoa_mais_pesada[0]}.")
    
# Encontrar a pessoa mais leve (peso < 70 kg)
pessoa_mais_leve = None
for pessoa in pessoas:
    if pessoa[1] < 70:
        if pessoa_mais_leve is None or pessoa[1] < pessoa_mais_leve[1]:
            pessoa_mais_leve = pessoa

if pessoa_mais_leve:
    print(f"O menor peso foi de {pessoa_mais_leve[1]}kg. Peso de {pessoa_mais_leve[0]}.")
else:
    print("Nenhuma pessoa com peso abaixo de 70kg foi cadastrada.")

