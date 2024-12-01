# Desafio 046: Contagem Regressiva - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles. 
# Usar uma lib para pausa.

import time

for contagem_regressiva in range(10, 0, -1):
    print(contagem_regressiva)
    time.sleep(1)
print('Fogos de artifício estourando!')

# O programa conta de 10 até 1, com uma pausa de 1 segundo entre cada número, e então exibe a mensagem "Fogos de artifício estourando!".