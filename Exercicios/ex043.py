# Desafio 043: Índice de Massa Corporal - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.1f}. Você está no peso ideal.')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f}. Você está com sobrepeso.')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.1f}. Você está com obesidade.')
else: 
    print(f'Seu IMC é {imc:.1f}. Você está com obesidade mórbida.')