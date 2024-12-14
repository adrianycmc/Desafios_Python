# Desafio 061: Progressão Aritmética v2.0 - Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo

while termo < primeiro_termo + 10 * razao:
    print(termo, end=' -> ')
    termo += razao
print('Fim')

# Explicação: O while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira. No caso do código acima, o bloco de código será repetido enquanto o termo for menor que o primeiro termo mais 10 vezes a razão. O termo é incrementado pela razão a cada iteração do loop. O código acima é equivalente ao código do Exercicios_Python/ex051.py, que utiliza a estrutura for para mostrar os 10 primeiros termos de uma progressão aritmética. Ambos os códigos produzem a mesma saída.