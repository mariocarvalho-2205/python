'''
Aula 21- Nessa aula, vamos continuar nossos estudos de funções em Python,
aprendendo mais sobre Interactive Help em Python,
o uso de docstrings para documentar nossas funções,
argumentos opcionais para dar mais dinamismo em funções Python,
escopo de variáveis e retorno de resultados.
'''
from colorama import init, Fore, Back, Style
init(autoreset=True)
print(Fore.RED + 'some red text')
print('automatically back to default color again')
print(Fore.RED + Back.BLACK + Style.NORMAL + 'testando')
print('testando2')

# help() é a ajuda do python no proprio sistema
# help(parametro) mostra a informação do parametro escolhido.
# EX. help(input) - Vai mostrar o manuel do comando input.
print(Back.GREEN + input.__doc__)  # Mostra a documentação do comando input com uma formatação
                      #diferente pode usar s help(input)
# docstring é a documentação da string
# criando docstring de uma função criada

# Criando docstring


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: Representa o inicio da contagem;
    :param f: Representa o final da contagem;
    :param p: Representa o passo da contagem;
    :return: Sem retorno
    Função criada por:
    """
    c = i
    while c <= f:
        print(Fore.RED + f'{c}', end=Fore.BLUE + '....')
        c += p
    print(Fore.GREEN + 'FIM!!')


contador(1, 20, 2)

#  mostra a docstring criada na função
help(contador)

# Parametros opcionais a=0, c=0, c=0, caso nao receba nenhum valor
# a variavel passa a receber valor zero 0.




def soma(a, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s, a}.')


soma(3, 2, 5)
soma(2, 3)
soma(2)


def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')


# Escopo de variavel
# Escopo local
def teste(b):
    #global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'b dentro vale {b}')
    print(f'C dentro vale {c}')


# Escopo global
a = 5  # Variavel global
teste(a)
print(f'A fora vale {a}')

def soma1(a, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}.')
    return s


n1 = soma1(3, 2, 5)
n2 = soma1(2, 2)
n3 = soma1(6)

print(f'Meus calculos deram {n1}, {n2} e {n3}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um numero fatorial: '))
print(f'O fatorial de {n} é ig1ual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados sao {f1}, {f2} e {f3}')
print()


def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input(f'Digite um numero: '))

if par(n):
    print('É par!!')
else:
    print('Não é par!!!')

