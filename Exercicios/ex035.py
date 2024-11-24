# Desafio 035: Analisando triângulo v1.0 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# Exemplo: 3 retas de comprimento 7, 4 e 5 formam um triângulo. Principio matemático utilizado: o comprimento de um lado de um triângulo é menor que a soma dos outros dois lados.

retas = input('Digite o comprimento de três retas: ').split()

retas_float = [float(numero) for numero in retas]

reta_menor = min(retas_float)
print(f'O menor é {reta_menor}')

retas_float.remove(reta_menor)

reta1, reta2 = retas_float
print(f'As outras duas retas são: {reta1} e {reta2}')

if reta1 + reta2 > reta_menor and reta1 + reta_menor > reta2 and reta2 + reta_menor > reta1:
    print('As retas formam um triângulo.')
else:
    print('As retas não formam um triângulo.')
    

# O programa lê o comprimento de três retas, converte os valores para float e armazena em uma lista. O programa então encontra o menor valor da lista e o remove. O programa então armazena os dois valores restantes em variáveis. O programa então verifica se a soma dos dois maiores valores é maior que o menor valor. Se for, o programa imprime que as retas formam um triângulo. Se não for, o programa imprime que as retas não formam um triângulo.