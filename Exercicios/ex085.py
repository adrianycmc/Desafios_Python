# Desafio 085: Listas com pares e ímpares - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []] 


for contador in range(1, 8):
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
        valores[0].append(valor) # Adiciona o valor na primeira lista, se for par. [0] = Pares
    else:
        valores[1].append(valor) # Adiciona o valor na segunda lista, se for ímpar. [1] = Ímpares
        
valores[0].sort() 
valores[1].sort()
        
print("\n" + "-=" * 30 + "\n")

print(f"Os valores pares digitados foram: {valores[0]}") 
print(f"Os valores ímpares digitados foram: {valores[1]}")