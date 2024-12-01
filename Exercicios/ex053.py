# Desafio 053: Detector de Palíndromo - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA. Tirar os espaços entre as palavras é o mesmo que juntar as palavras.

frase = str(input('Digite uma frase: ')).strip().upper()

frase_sem_espacos = ''.join(frase.split())

inverso = ''

for letra in range(len(frase_sem_espacos) - 1, -1, -1):
    inverso += frase_sem_espacos[letra]

if frase_sem_espacos == inverso:
    print(f'O inverso de {frase_sem_espacos} é {inverso}.')
    print('A frase é um palíndromo.')
else:  
    print(f'O inverso de {frase_sem_espacos} é {inverso}.')
    print('A frase não é um palíndromo.')
    
print('=' * 20)

# Solução alternativa:
frase = str(input('Digite uma frase: ')).strip().upper()

frase_sem_espacos = ''.join(frase.split())

inverso = frase_sem_espacos[::-1]

if frase_sem_espacos == inverso:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
    