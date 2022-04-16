frase = str(input('Digite uma frase: ')).strip().upper()
print('A frase acima tem {} letras A.'.format(frase.count('A')))
print('A primeira letra A, aparece na {} posição e o ultimo A aparece na {}.'.format((frase.find('A')+1), frase.rfind('A')+1))
print('A ultima letra A, aparece na {} posição.'.format(frase.rfind('A')+1))
# O rfind, conta da direita para a esquerda.
'''No caso da formatação >>> .format((frase.find('A')+1), frase.rfind('A')+1)) >>> Cada argumento tem que estar 
completamente dentro de cada parentese'''