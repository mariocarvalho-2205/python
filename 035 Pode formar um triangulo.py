print('Digite 3 medidas para saber se pode formar um triangulo: ')
l1 = float(input('1 segmento: '))
l2 = float(input('2 segmento: '))
l3 = float(input('3 segmento: '))
if l2 + l3 > l1 and l1 + l3 > l2 and l1 + l2 > l3:
    print('É possivél formar um triangulo')

else:
    print('Não é possivel formar um triangulo.')

'''Logica para atender a condição de formação de um triangulo:
b + c > a
a + c > b
a + b > c
Exemplo:
a) 13 cm, 9 cm e 7 cm?
Devemos ter: 13 + 9 > 7, 13 + 7 > 9 e 9 + 7 > 13, 
para que seja um triângulo. Vamos verificar:
13 + 9 = 22 ⇒ 13 + 9 > 7
13 + 7 = 20 ⇒ 13 + 7 > 9
9 + 7 = 16 ⇒ 9 + 7 > 13
É possível formar um triângulo com essas medidas.

b) 15 cm, 8 cm e 6 cm?
Devemos ter: 15 + 8 > 6, 15 + 6 > 8 e 8 + 6 > 15, para que seja um triângulo. Vamos verificar:
15 + 8 = 23 ⇒ 15 + 8 > 6
15 + 6 = 21 ⇒ 15 + 6 > 8
8 + 6 = 14 ⇒ 8 + 6 < 15 ⇒ não satisfaz a condição!
Não é possível formar um triângulo com essas medidas.
'''