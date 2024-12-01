# Desafio 048: Soma de ímpares múltiplos de três - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500. Saber se é divisível por 3 é o mesmo que saber se o resto da divisão por 3 é zero.

soma = 0 
# Pegando todos os números ímpares de 1 a 500.
for num in range(1, 501, 2):
    # print(num)
    # Verifica se o número é divisível por 3.
    if num % 3 == 0:
        # print(f'{num} é divisível por 3.') 
        soma += num
print(f'A soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é {soma}.')
        