real = float(input('Digite quanto tem em Real R$ '))

dolar = 5.37

print('R$ {:.2f} \033[1;32mReais\033[m, da para comprar U$ {:.2f} \033[1;31mDolar(es)\033[m'.format(real, real/dolar))
