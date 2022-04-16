import datetime
ano = datetime.date.today().year

from datetime import date
atual = date.today().year
maior = 0
menor = 0
#maior = []
#menor = []
for c in range(1, 7):
    nasc = int(input('Em que ano a {} pessoa nasceu?  '.format(c)))
    if (atual - nasc) >= 21:
        maior += 1
        #maior.append(nasc)
    else:
        menor += 1
        #menor.append(nasc)
print('Temos {} pessoas maior de idade, e {} menor de idade'.format(maior, menor))
#print('Temos {} pessoas maior de idade, e {} menor de idade'.format(len(maior), len(menor)))

#print(atual - nasc, ano, ano - nasc)
