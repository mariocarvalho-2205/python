#Corrigido
print('Digite 3 medidas para saber se pode formar um triangulo: ')
l1 = float(input('1 segmento: '))
l2 = float(input('2 segmento: '))
l3 = float(input('3 segmento: '))
#if l2 + l3 > l1 and l1 + l3 > l2 and l1 + l2 > l3:
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
#alternativa para condicional do triangulo
    print('É possivél formar um triangulo!')
    #if l1 == l2 and l2 == l3: Condição normal
    if l1 == l2 == l3: #Condição abreviada
        print('Esse é um triangulo Equilatero.')
    #Essa condição pode ser evitada usando o else
    #elif l1 == l2 or l2 == l3 or l3 == l1:
    #elif l1 == l2 != l3:
    #   print('Esse é um triangulo Isosceles.')'''

    #elif l1 != l2 and l2 != l3: Condição normal
    elif l1 != l2 != l3 != l1:
        print('Esse é um triangulo Escaleno.')
    else:
        print('Esse é um triangulo Isosceles.')
else:
    print('Não é possivel formar um triangulo.')