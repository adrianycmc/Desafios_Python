# Desafio 080: Lista ordenada sem repetições - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for contador in range(0, 5):
    num = int(input("Digite um valor: "))
    if contador == 0 or num > lista[-1]:
       lista.append(num)
       print("Adicionado ao final da lista...")
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f"Adicionado na posição {posicao} da lista...")
                break
            posicao += 1
print(f"Os valores digitados em ordem foram {lista}.") 