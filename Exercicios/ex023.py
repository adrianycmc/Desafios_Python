# Desafio 023: Separando dígitos de um número - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834 -> unidade: 4, dezena: 3, centena: 8, milhar: 1.

# 1ª Solução:
numero = (input("Digite um número de 0 a 9999: "))

if len(numero) != 4:
    print("Número inválido.")
    23
else:
    print(f'Milhar: {numero[0]}')
    print(f'Centena: {numero[1]}')
    print(f'Dezena: {numero[2]}')
    print(f'Unidade: {numero[3]}')
    

print('='*50)
    
# O método len() retorna o número de itens de um objeto. Quando o objeto é uma string, o método len() retorna o número de caracteres da string. Neste caso, o método len() foi utilizado para verificar se o número digitado tem 4 caracteres. Se o número digitado tiver 4 caracteres, o programa imprime cada um dos dígitos separadamente. Caso contrário, o programa imprime "Número inválido".

# 2ª Solução:
numero = input("Digite um número de 0 a 9999: ")

if len(numero) == 1:
    print(f'Unidade: {numero}')
elif len(numero) == 2:
    print(f'Dezena: {numero[0]}')
    print(f'Unidade: {numero[1]}')
elif len(numero) == 3:
    print(f'Centena: {numero[0]}')
    print(f'Dezena: {numero[1]}')
    print(f'Unidade: {numero[2]}')
elif len(numero) == 4:
    print(f'Milhar: {numero[0]}')
    print(f'Centena: {numero[1]}')
    print(f'Dezena: {numero[2]}')
    print(f'Unidade: {numero[3]}')
else:
    print("Número inválido.")
    
print('='*50)
    
# Neste caso, o programa verifica o número de caracteres do número digitado e imprime cada um dos dígitos separadamente de acordo com a quantidade de caracteres. Se o número digitado tiver 1 caractere, o programa imprime a unidade. Se o número digitado tiver 2 caracteres, o programa imprime a dezena e a unidade. Se o número digitado tiver 3 caracteres, o programa imprime a centena, a dezena e a unidade. Se o número digitado tiver 4 caracteres, o programa imprime a milhar, a centena, a dezena e a unidade. Caso contrário, o programa imprime "Número inválido".

# 3ª Solução:
numero = input('Digite um número de 0 a 9999: ')

if not numero.isdigit() or not (0 <= int(numero) <= 9999):
    print("Número inválido.")
else:
    numero = numero.zfill(4)
    
    print(f'Milhar: {numero[0]}')
    print(f'Centena: {numero[1]}')
    print(f'Dezena: {numero[2]}')
    print(f'Unidade: {numero[3]}')
    
# Neste caso, o programa verifica se o número digitado é um número inteiro e se está entre 0 e 9999. Se o número digitado não for um número inteiro ou não estiver entre 0 e 9999, o programa imprime "Número inválido". Caso contrário, o programa preenche o número digitado com zeros à esquerda até que ele tenha 4 caracteres e imprime cada um dos dígitos separadamente. O método isdigit() retorna True se todos os caracteres da string forem dígitos e houver pelo menos um caractere, caso contrário, retorna False. O método zfill() preenche a string com zeros à esquerda até que ela tenha um comprimento especificado. Neste caso, o método zfill() foi utilizado para preencher o número digitado com zeros à esquerda até que ele tenha 4 caracteres.