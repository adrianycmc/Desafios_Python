# Desafio 005: Antecessor e sucessor. - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

# # 1ª solução:
num_int = int(input('Digite um número:'))
print (f'O número digitado foi {num_int}. Seu antecessor é {num_int - 1} e seu sucessor é {num_int + 1}')

# 2ª solução:

num_ex = input('Digite um número: ')

if num_ex.isnumeric():
    num_int = int(num_ex)
    print(f'O número digitado foi {num_int}. Seu antecessor é {num_int - 1} e seu sucessor é {num_int + 1}')
else:
    print('Para ser válido, digite um número inteiro.')

# # 3ª solução:
# # O bloco try-except em Python é usado para capturar e tratar exceções (erros) que podem ocorrer durante a execução do código. Ele permite que você execute um bloco de código e, se ocorrer um erro, você pode lidar com esse erro de maneira controlada, sem que o programa seja interrompido abruptamente.
    
    
num_str = input('Digite um número:')

try:
    num_int = int(num_str)
    print(f'O número digitado foi {num_int}. Seu antecessor é {num_int - 1} e seu sucessor é {num_int + 1}')
except ValueError:
    print('Para ser válido, digite um número inteiro.')
    
    