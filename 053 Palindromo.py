frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palindromo.')
else:
    print('A frase digitada NÃO É UM PALINDROMO.')

'''#import unidecode
#Biblioteca unidecode serve para converter as palavras para outro encode e remover espaços
frase1 = str(input('Digite uma frase para ver se ela é Palindromo. ')).upper().strip()
#fresesemacento = unidecode.unidecode(frase)
espaco = frase1.replace(' ', '')#, unidecode.unidecode(frase1)
print(espaco)
if espaco[0: ] == espaco[::-1]:
    print('A frase {} é um PALINDROMO.'.format(frase1))
else:
    print('A frase {} não é um PALINDROMO.'.format(frase1))

frase = str(input('Dgite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, - 1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo. ')
else:
    print('A frase não é um palindromo.')
    
print(junto[letra],  inverso, end='')
print('\nVocê digitou a frase {}'.format(junto))'''
