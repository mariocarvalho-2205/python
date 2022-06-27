'''
101- Crie um programa que tenha uma função chamada voto() que vai
receber como parametro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
'''


def voto(ano):
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return Fore.LIGHTYELLOW_EX + f'Com {idade} anos: Ainda não vota!!!'
    elif 16 <= idade < 18 or idade > 65:
        return Fore.BLUE + f'Você tem {idade} anos. O voto é opcional!!!'
    else:
        return Fore.RED + f'Você tem {idade} anos. VOTO OBRIGATORIO!!'



nasc = int(input('Qual o seu ano de nascimento? '))
print(voto(nasc))
print('Obrigado e volte sempre!!!')


