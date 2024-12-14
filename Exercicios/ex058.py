# Desafio 058: Jogo da adivinhação v2.0 - Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# import random 

# num = random.randint(0, 10)
# num_user = 0
# tentativas = 0

# while num != num_user:
#     num_user = int(input('Digite um número entre 0 e 10: '))
#     tentativas += 1
#     print('Que pena! Você errou! Tente novamente.')
    
# print(f'Parabéns! Você acertou com {tentativas} tentativas.')


import random 

num = random.randint(0, 10)
num_user = 0
tentativas = 0

while num != num_user:
    num_user = int(input('Digite um número entre 0 e 10: '))
    if num != num_user:
        tentativas += 1
        print('Que pena! Você errou! Tente novamente.')
    else:
        print(f'Parabéns o número correto é {num}! Você acertou com {tentativas} tentativas.')