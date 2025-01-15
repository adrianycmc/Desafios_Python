# Desafio 098: Função de Contador - Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada: A) De 1 até 10, de 1 em 1; B) De 10 até 0, de 2 em 2; C) Uma contagem personalizada - o usuário vai digitar o inicio, fim e passo. 


from time import sleep

def linha():
    print("-=" * 30)
    
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -passo 
    elif inicio > fim:
        passo = -passo 
        
    print(f"Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:")
    for contador_passos in range(inicio, fim + (1 if passo > 0 else -1), passo):
        print(contador_passos, end=' ', flush=True)
        sleep(0.5)
    print()

linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()

print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
linha()
contador(inicio, fim, passo) 
print("FIM!")