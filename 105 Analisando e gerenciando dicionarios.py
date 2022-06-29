'''
105-) Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um
dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
'''

def notas(*n, sit=False):
    '''
notas(n*, sit=False)
    -> Função para analisar notas e situações de varios alunos.    
    :param n: Uma ou mais notas dos alunos(aceita varias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com varias informações sobre a situação da turma.
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:  # valida se sit=True, se for retorna a situação do aluno.
        if r['media'] >= 7:
            r['situação'] = 'BOA!'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL!!!'
        else:
            r['situalção'] = 'RUIM!!!'
    return r


resp = notas(8, 8, 8, 8, sit=True)
print(resp)
help(notas)
