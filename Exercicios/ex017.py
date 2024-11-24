# Desafio 017: Catetos e Hipotenusa - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}.')

# math.hypot() é uma função que calcula a hipotenusa de um triângulo retângulo, dado os comprimentos dos catetos.