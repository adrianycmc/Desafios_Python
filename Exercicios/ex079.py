# Desafio 079: Valores únicos em uma Lista - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []

while True:
    num = int(input("Digite um valor:"))
    
    if num not in valores:
        valores.append(num) # Adiciona na lista
        print("Valor adicionado com sucesso...")
    else:
        print("Ops valor duplicado! Não vou adicionar...")
        
    continuar = str(input("Deseja continuar? [S/N]: ")).upper()
    while continuar not in ['S', 'N']:
        print("Opção inválida. Digite novamente!")
        continuar = str(input("Deseja continuar? [S/N]: ")).upper()
    if continuar == 'N':
        break
    
valores.sort() # Ordena a lista
print(f"Sua lista ficou com os valores = {valores}.")