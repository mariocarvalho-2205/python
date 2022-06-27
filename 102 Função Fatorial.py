'''
101- Crie um programa que tenha uma função fatorial() que receba dois parametros:
o primeiro que indique o numero a calcular e o outro chamado show, que será um
valor logico(opcional) indicado se será mostrado ou não na tela o processo de calculo
fatorial.
'''

def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x ', end='')
        f *= c
    return f
print(fatorial(5, show=True))


