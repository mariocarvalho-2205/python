'''
104: Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)
'''
from colorama import init, Fore, Back
init(autoreset=True)

# Segue a mesma linha de raciocinio do exercicio anterior


def leiaint(msg):
    ok = False  # começa com validação falsa
    valor = 0  # variavel vai receber o valor lido pela função
    while True:  # vai repetir ate que a condição seja verdadeira
        n = str(input(msg))  # recebe o dado da função leiaInt
        if n.isnumeric():  # Faz a validação se é numero ou não
            valor = int(n)
            ok = True  # se for numero, o validador passa a ser verdadeiro
        else:  # se o validador for falso vai cair nesse else:
            print(Fore.BLACK + Back.RED + 'Digite um valor numerico!!')
        if ok:  # se o validador for verdadeiro encerra o laço
            break
    return valor  # Retorna com o valor recebido pela variavel


n = leiaint('Digite um numero: ')   # Variavel n, vai receber o valor da função leiaInt
print(f'Voce acabou de digitar {n}')
