larg = float(input('Digite a largura em metros: '))
alt = float(input('Digite a altura em metros: '))
area = larg * alt
litro = 2

print('Para a area de {:.0f} metros quadrados, você vai precisar de {}{:.0f}{} litros de tinta.'.format(area, '\033[33m', area/litro, '\033[m'))