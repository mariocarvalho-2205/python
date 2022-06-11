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
dados = {'Nome': 'Mario', 'Idade': 47, 'sexo': 'Masculino', 'sobrenome': 'tenorio'}
# nome_dicionario['titulo adicionado'] = 'dado adicionado'
del dados['sexo']
print(dados)

filme = {
    'titulo': 'Star Wars',
    'ano': '1977',
    'diretor': 'George Lucas'
}
print()
print(filme['titulo'])
print(filme.values())  # imprime os valores que contem no dicionario (dados)
print()
print(filme.keys())  # imprime as chaves que contem no dicionario (titulos dos dados)
print(filme.items())  # imprime cada item (titulo + dados) em forma de tupla
filme['peso'] = 47
for chaves, valores in filme.items():  # keys e values
    print(f'O {chaves} é {valores}.')

locadora = [
    {'titulo': 'Star Wars',
     'ano': '1977',
     'diretor': 'George Lucas'},
    {'titulo': 'sonic',
     'ano': '2019',
     'diretor': 'não sei'},
    {'titulo': 'home de ferro',
     'ano': '2015',
     'diretor': 'tambem nao sei'}
]
print()
for k in range(0, len(locadora)):
    print(f'O filme {locadora[k]["titulo"]} foi feito em {locadora[k]["ano"]}')
print()

# Criando dicionario dentro de uma lista

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'Sigla': 'SP'}
brasil.append(estado1)  # Adiciona o dicionario na lista
brasil.append(estado2)
print(brasil[0]['uf'])

# Criando uma copia do dicionario dentro de uma lista
estado = dict()
brasil = list()
for c in range(0, 3):  # For criado para adicionar itens
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())  # Para adicionar o dicionario a lista usa-se o .copy()
    # depois da variavel do dicionario e não usa o fatiamento [:]
print(f'Dicionario Brasil completo {brasil}')
print('Agora o dicionario individual: ')
for e in brasil:  # assim vai mostrar cada dicionario inteiro
    print(e)
print('Imprimindo individual e formatado: ')
for i in brasil:  # usando dois laços vai mostrar

    for k, v in i.items():
        print(f'O campo {k} tem valor {v}.')
    print()

for c in brasil:
    for v in c.values():
        print(v, end=' ')
    print()

