# Desafio 105: Analisando e gerando dicionários - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: - Quantidade de notas - A maior nota - A menor nota - A média da turma - A situação (opcional) adicional, que pode ser: RUIM, RAZOÁVEL ou BOA.


def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    
    """
    
    dict = {}
    dict['total'] = len(notas)
    dict['maior'] = max(notas)
    dict['menor'] = min(notas)
    dict['media'] = sum(notas) / len(notas)
    
    if sit:
        if dict['media'] < 5:
            dict['situação'] = 'RUIM'
        elif 5 <= dict['média'] < 7:
            dict['situacao'] = 'RAZOÁVEL'
        else:
            dict['situacao'] = 'BOA'
            
    return dict

print("-----------------------------------")
resp = notas(9.0, 7.5, 5.0, 8.0, sit=True)
print(resp)