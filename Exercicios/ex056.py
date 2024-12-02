# Desafio 056: Analisador completo - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

nomes = []
idades = []
sexos = []

for pessoa in range(1, 5):
    nome = str(input(f'Digite o nome da {pessoa}ª: '))
    idade = int(input(f'Digite a idade da {pessoa}ª: '))
    sexo = str(input(f'Digite o sexo da {pessoa}ª [M/F]: ')).upper()
    
    # Armazenando na lista
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

# Média de idade do grupo
print(f'A média de idade do grupo é {sum(idades)/len(idades)} anos.')

# Homem mais velho
# Variáveis para armazenar o homem mais velho
maior_idade = -1
nome_homem_mais_velho = ''

# Iterando sobre a lista de sexos para encontrar o homem mais velho
for sexo in range(4):
    if sexos[sexo] == 'M' and idades[sexo] > maior_idade: # Se o sexo for masculino e a idade for maior que a maior idade encontrada até o momento.
        maior_idade = idades [sexo] # Atualizando a maior idade.
        nome_homem_mais_velho = nomes[sexo] # Atualizando o nome do homem mais velho.

# Imprimindo o nome do homem mais velho
print(f'O homem mais velho é {nome_homem_mais_velho} com {maior_idade} anos.')

# Mulheres com menos de 20 anos
mulheres_menos_20 = 0

for sexo in range(4):
    if sexos[sexo] == 'F': # Se o sexo for feminino.
        if idades[sexo] < 20: # Se a idade for menor que 20.
            mulheres_menos_20 +- 1 # Contando quantas mulheres têm menos de 20 anos.
            
print(f'{mulheres_menos_20} mulheres têm menos de 20 anos.')
            
            