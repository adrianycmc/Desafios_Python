# Desafio 072: Número por extenso - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Se digitar outro número, o programa deverá mostrar uma mensagem de erro. 


numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezeseis", "Dezesete", "Dezoito", "Dezenove", "Vinte")
numero = int(input("Digite um número entre 0 e 20: "))
if numero < 0 or numero > 20:
    print("Tente novamente.")    
else: 
    print(f"O número por extenso é {numeros[numero]}.") # [numero] é o índice da tupla.