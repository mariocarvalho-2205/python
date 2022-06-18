'''
096- Faça um programa que tenha uma função chamada area(), que receba as dimensões
de um terreno retangular(largura, comprimento) e mostre a area do terreno.
'''


def area(largura, comp):
    areatotal = largura * comp
    print(f'A área de um terreno {largura}x{comp} é de {areatotal}m².')


print('-=' * 15)
print(f'{"Controle de Terrenos":^30}')
print('-=' * 15)
largura = float(input('Digite a largura do terreno (m): '))
comp = float(input('Digite o comprimento d terreno (m): '))

area(largura, comp)

