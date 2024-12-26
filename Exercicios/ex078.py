# Desafio 078: Maior e Menor valores na Lista - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []

for contador in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {contador}: ")))
    
print("\n" + "-=" * 30)
print(f"O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}.")
print(f"O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}.")