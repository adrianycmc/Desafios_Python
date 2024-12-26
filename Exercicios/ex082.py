# Desafio 082: Dividindo valores em várias listas - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas. Primeiro loop analisa os valores e depois insere nas listas respectivas.

total_de_valores = []
pares = []
impares = []

while True:
    valor = int(input("Digite um valor: "))
    total_de_valores.append(valor) # Adiciona o valor na lista
    print("Valor adicionado com sucesso...")
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    
    continuar = str(input("Deseja continuar? [S/N]: ")).upper()
    while continuar not in ['S', 'N']:
        print("Opção inválida. Digite novamente!")
        continuar = str(input("Deseja continuar? [S/N]: ")).upper()
    if continuar == 'N':
        break
    
print(f"\nOs valores digitados foram: {total_de_valores}.")
print(f"Os valores pares digitados foram: {pares}.")
print(f"Os valores ímpares digitados foram: {impares}.")