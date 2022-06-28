'''
101- Crie um programa que tenha uma função fatorial() que receba dois parametros:
o primeiro que indique o numero a calcular e o outro chamado show, que será um
valor logico(opcional) indicado se será mostrado ou não na tela o processo de calculo
fatorial.
'''


def fatorial(n, show=False):
    '''
    >= Faz o calculo fatorial do numero escolhido.
    :param n: Variavel recebe o numero digitado pelo usuario.
    :param show: True> exibe o calculo do fatorial. False> exibe apenas o resultado.
    :return: retora a função com o resultado.
    '''
    f = 1
    print(f'Calculando {n}! = ', end='')
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# help(fatorial)


num = int(input('Digite um numero para fatorial: '))
print(fatorial(num, show=False))


