# Desafio 062: Super Progressão Aritmética v3.0 - Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo
total = 0
mais_termos = 10
contador = 0

while mais_termos != 0:
    total += mais_termos
    while contador <= total:
        print(termo, end=' -> ')
        termo += razao
        contador += 1
    print('Pausa')
    mais_termos = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')


    