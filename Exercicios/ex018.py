# Desafio 018: Seno, Cosseno, Tangente - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo}° tem o seno de {seno}°, o cosseno de {cos:}° e a tangente de {tang}°.')

# math.sin(), math.cos() e math.tan() são funções que calculam o seno, cosseno e tangente de um ângulo, respectivamente. Porém, essas funções recebem o ângulo em radianos, então é necessário converter o ângulo de graus para radianos antes de passá-lo como argumento para essas funções. A função math.radians() faz essa conversão.