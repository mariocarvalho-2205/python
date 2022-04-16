'''nome = input('Digite um nome com letras minusculas: ')

print('O nome digitado {} escrito com letras maiusculas é {}'.format(nome, str.upper(nome)))

nome2 = input('Digite um nome com letras maiusculas: ')
print('O nome digitado com letras maiusculas {} ficara assim {}'.format(nome2, str.lower(nome2)))
'''
nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome')
print('O nome escrito com letras maiusculas {}'.format(nome.upper()))
print('O nome escrito com letras minusculas {}'.format(nome.lower()))
print('O nome escrito sem espaços tem {} caracteres.'.format(len(nome.replace(' ', ''))))
print('Outra maneira de contar sem espaços é {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

lista = nome.split() #convertendo a nome em lista para contar as palavras separadas
print('O primeiro nome é {}, e tem {} letras.'.format(lista[0], len(lista[0])))
print('O ultimo nome é {} e tem {} letras.'.format(lista[-1], len(lista[-1])))
print(f'Usando f String-O ultimo nome é {lista[-1]} e tem {len(lista[-1])} letras.')
#print(lista)



