import calendar
from datetime import date #para pegar o ano atual
ano = int(input('Digite um ano: Coloque 0 para o ano atual: '))
if ano == 0: # Condição para pegar o ano atual
    ano = date.today().year

#Condição composta
if calendar.isleap(ano) == True:
    print(f'O ano de {ano} é Bissexto')
else:
    print(f'O ano de {ano} não é Bissexto')
#Condição simples
print(f'O ano {ano} é bissexto.' if calendar.isleap(ano) == True else f'O ano {ano} não é bissexto.')

#print(calendar.isleap(ano))

#usando o metodo matematico
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é Bissexto.'.format(ano))
else:
    print('O ano de {} não é Bissexto.'.format(ano))
