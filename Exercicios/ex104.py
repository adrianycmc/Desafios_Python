# Desafio 104: Validando entrega de dados em Python - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 


def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero 
        except (ValueError, TypeError):
            print("ERRO! Digite um número válido.")
            
        
num = leiaInt("Digite um número: ")
print(f'Você acabou de digitar o número {num}.')