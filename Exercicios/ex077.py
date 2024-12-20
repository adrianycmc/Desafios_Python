# Desafio 077: Contando vogais em Tupla - Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("ameba", "cachorro", "televisao", "rato", "paralelepipedo", "sorvete", "natal")

vogais = "aeiouAEIOU"

print("-" * 40)
print(f"{'SEPARANDO AS VOGAIS':^40}") 	
print("-" * 40)

for palavra in palavras: # Para cada palavra na tupla palavras.
    print(f"\n Na palavra {palavra.upper()} temos as vogais: ", end="")
    for letra in palavra: # Para cada letra na palavra.
        if letra in vogais: # Se a letra estiver em vogais.
            print(letra.upper(), end=" ")