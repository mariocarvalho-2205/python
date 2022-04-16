qtddias =int(input('Por quantos dias foram alugados? '))
qtdkm = int(input('Quantos Km foram percorridos? '))
#km = qtdkm * 0.15
#dias = qtddias * 60
total = qtddias * 60 + qtdkm * 0.15
print('Valor a ser pago por {} dias e {} km rodados é \033[34;42mR$ {:.2f}\033[m'.format(qtddias, qtdkm, total))

