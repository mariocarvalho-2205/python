#Corrigida!
#import datetime
#date = datetime.date.today()
#ano = date.year
from datetime import date
ano = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = ano - nascimento
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Entra para a categoria Mirim!')
elif idade <=14:
    print('Entra para a categoria Infantil!')
elif idade <= 19:
    print('Entra para a categoria Junior!')
elif idade <= 25:
    print('Entra para a categoria Senior!')
else:
    print('Entra para a categoria Master!!')