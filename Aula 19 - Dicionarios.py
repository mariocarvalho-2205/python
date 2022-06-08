'''
Aula 19 - Dicionarios.
Para criar dicionario:
# usando função
dados = dict()

lista = {
    'Chave(keys)' : 'Valor(values)'
    'Nome' : 'Mario',
    'Idade' : 47,
    'sexo' : 'Masculino'
}
Para adicionar dados:
dados[sobrenome] = 'tenorio'

para remover elementos:
del lista['sexo']
'''
dados = {
    'Nome' : 'Mario',
    'Idade' : 47,
    'sexo' : 'Masculino'
}
dados['sobrenome'] = 'tenorio'
del dados['sexo']
print(dados)