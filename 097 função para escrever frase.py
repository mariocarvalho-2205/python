'''
097- Faça umprograma que tenha uma função chamada escreva(),
que receba um texto qualquer como parametro e mostre uma mensagem
com o tamanho adaptavel.
'''


def escreva(frase):
    tam = len(frase) + 4
    print('~' * tam)
    print(f'  {frase}')
    print('~' * tam)


f = str(input('Digite uma frase: '))
escreva(f)
