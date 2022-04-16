metros = float(input('Digite a medida em metros: '))

cent = 100
mili = 1000
km = 1000


print('{} metros da {} \033[41mcentimetros\033[m.'.format(metros, (metros*cent)))
print('{:.0f} metros da {:.0f} \033[44mmilimetros\033[m.'.format(metros, (metros*mili)))
print('{:.2f} em metros da {} \033[7;40mquilometros\033[m.'.format(metros, (metros/km)))
