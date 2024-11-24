# Desafio 014: Conversor de temperatura - Escreva um programa que converta uma temperatura digitada em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Informe a temperatura em graus Celsius: '))
fahrenheit = celsius * 1.8 + 32
print(f'A temperatura de {celsius}°C corresponde a {fahrenheit}°F.')