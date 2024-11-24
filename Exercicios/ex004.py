# Desaio 004: Dissecando uma variável - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

var_algo = float(input('Digite algo: '))
print(f'O tipo dess valor é {type(var_algo)}')

var_algo_type = input('Digite mais alguma coisa: ')
print(f'Esse valor é um número? {var_algo_type.isnumeric()}')


# Criando verificações para saber se a variável é um número, letra ou alfanumérico.
# if var_algo_type.isnumeric() == True:
#     print("Sim, é um número.")
# else:
#     print("Não é um número.")
    
# if var_algo_type.isalpha == True:
#     print("Sim, é uma letra.")
# else:
#     print("Não é uma letra.")

# if var_algo_type.isalnum() == True:
#     print("Sim, é alfanumérico.")
    
# Encadeando as verificações com elif.    
if var_algo_type.isnumeric():
    print("É um número.")
elif var_algo_type.isalpha():
    print("É uma letra.")
elif var_algo_type.isalnum():
    print("É alfanumérico.")
else:
    print("Não é um número, letra ou alfanumérico.")