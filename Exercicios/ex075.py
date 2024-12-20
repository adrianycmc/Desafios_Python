# Desafio 075: Análise de dados em uma Tupla - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares. Se buscar o valor que não existe tem que dar uma mensagem de erro.

valores = ()


for var in range(4):
    # Adicionando valores à tupla.
    valores += (int(input(f"Digite o {var + 1}º valor: ")),) 
    
print(f"Você digitou os valores: {valores}")

if 9 in valores:
    print(f"O valor 9 apareceu {valores.count(9)} vezes.")
else: 
    print("O valor 9 não foi digitado.")
    
if 3 in valores:
    print(f"O valor 3 foi digitado na posição {valores.index(3) + 1}.")
else:
    print("O valor 3 não foi digitado.")
    
for num in valores:
    if num % 2 == 0:
        print(f"Os números pares digitados foram: {num}.")
    else:
        print("Não foram digitados números pares.")
                
                