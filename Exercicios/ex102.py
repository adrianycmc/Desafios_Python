# Desafio 102: Função para fatorial - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n=1, show=False):
    """
    Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    
    """
    fat = 1
    resultado = ""
    for contador in range(n, 0, -1):
        fat *= contador
        if show:
            if contador == n:
                resultado += f"{contador}! = {contador} "
            else:
                resultado += f"x {contador} "
    if show:
        resultado += f" = {fat}"
        return resultado
    else:
        return fat


print("-----------------------------------")
print(fatorial(5))
print(fatorial(5, show=True))