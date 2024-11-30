# Desafio 042: Analisando Triângulos - Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais.
# - Isósceles: dois lados iguais.
# - Escaleno: todos os lados diferentes.

reta_1 = float(input('Digite o comprimento da primeira reta: '))
reta_2 = float(input('Digite o comprimento da segunda reta: '))
reta_3 = float(input('Digite o comprimento da terceira reta: '))

if reta_1 + reta_2 > reta_3 and reta_1 + reta_3 > reta_2 and reta_2 + reta_3 > reta_1:
    print('As retas formam um triângulo.')
    
    if reta_1 == reta_2 == reta_3:
        print('O triângulo é Equilátero.')
    elif reta_1 == reta_2 or reta_1 == reta_3 or reta_2 == reta_3:
        print('O triângulo é Isósceles.')
    else:
        print('O triângulo é Escaleno.')   
else:
    print('As retas não formam um triângulo.')
    