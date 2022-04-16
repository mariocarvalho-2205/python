import datetime
from datetime import date
data = datetime.date.today() # aqui você obtem a data atual completa com mes, dia e ano
#ano = data.year ''' aqui você obtem somente o ano atraves da variavel criada
'''com datetime.date.today(), e faz o filtro na variavel atual com o dado que quer pegar'''
atual = date.today().year

sexo = str(input('Informe o sexo do candidato: (F) para feminino e (M) para masculino: ')).upper()
nome = str(input('Qual o seu nome? ')).capitalize()

if sexo == 'M':
    nasc = int(input('\033[35mDigite o seu ano de nascimento: \033[m'))
    idade = atual - nasc
    if idade < 18:
        saldo = 18 - idade
        print('\033[36m{}, você tem {} ano(s) e irá se alistar daqui a {} ano(s).\033[m'.format(nome, idade, saldo))
        ano = atual + saldo
        print(f'Seu alistamento será em {ano}!')
    elif idade > 18:
        saldo = idade - 18
        print('\033[34m{}, você passou do prazo, está {} ano(s) atrasado.\033[m'.format(nome, saldo))
    #else: pode ser usado tambem com o else:
    elif idade == 18: # Dessa maneira o codigo fica mais facil de ser entendido por outra pessoa.
        print('\033[33m{}, você está com {} anos. Alistamento IMEDIATO!!.\033[m'.format(nome, idade))
elif sexo == 'F':
    print(f'{nome}. Você não precisa fazer alistamento militar obrigatorio!')
else:
    print(f'{nome} Essa opção é invalida. Tente novamente escolhendo uma das opções acima! ')
#print(f'O ano atual é \033[33m{ano}\033[m')


#print(datetime.date.today())

#print(idade)
'''
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
print(f"Current Year -> {year}")
print(datetime.datetime.now())'''
