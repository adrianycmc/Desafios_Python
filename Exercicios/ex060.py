# Desafio 060: Cálculo do Fatorial - Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número para calcular o seu fatorial: '))
resultado = 1

while num > 1:
    resultado *= num
    num -= 1
    
print(f'O fatorial é {resultado}.')

# Explicação: O programa utiliza um laço de repetição while para calcular o fatorial do número digitado pelo usuário. A variável resultado é inicializada com 1 e, a cada iteração do laço, é multiplicada pelo valor de num. O valor de num é decrementado em 1 a cada iteração, até que seja menor ou igual a 1. Ao final do laço, o programa exibe o resultado do fatorial calculado.