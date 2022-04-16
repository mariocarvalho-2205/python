print('Conversor Decimal')
num = int(input('Digite um numero decimal qualquer: '))

base = int(input('''Escolha uma das bases para conversao: 
[ 1 ] para binario: 
[ 2 ] para Hexadecimal 
[ 3 ] para Octadecimal: 
Sua Opção: '''))

'''binario = bin(num).replace('0b', '')
hexa = hex(num).replace('0x', '')
octa = oct(num).replace('0o', '')
OBS: Para remover os dois primeiros digitos, ao inves de usar o replace, usa o fatiamento da string [2:]'''
if base == 1:
    print('O numero {} convertido em binario fica {}.'.format(num, bin(num)[2:]))
elif base == 2:
    print('O numero {} convertido em hexadecimal fica {}.'.format(num, hex(num)[2:]))
elif base == 3:
    print('O numero {} convertido em octadecimal fica {}.'.format(num, oct(num)[2:]))
else:
    print('Opção invalida!')

'''print(f'{binario}', hexa, octa)
    
print('{}'.format(hexa, 'x'))
print('{}'.format(octa, 'o'))
'''

