# Desafio 052: Números primos - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. O número primo é aquele que é divisível apenas por 1 e por ele mesmo.

num = int(input('Digite um número: '))

if num > 1:
    # O range começa a partir do 2, pois o número 1 não é primo.
    for contador in range(2, num):
        if num % contador == 0: # Dentro do laço, verifica se num é divisível por contador. A expressão num % contador calcula o resto da divisão de num por contador. Se num % contador for igual a 0, significa que num é divisível por contador sem deixar resto, ou seja, contador é um divisor de num. Exemplo: se o número que o usuário digitou for 6, o laço vai verificar se 6 é divisível por 2, 3, 4 e 5. Se for divisível por qualquer um desses números, o número não é primo.

            print(f'O número {num} não é primo.')
            break # interrompe o laço, pois já foi encontrado um divisor e não é necessário continuar verificando.
    else:
        print(f'O número {num} é primo.')