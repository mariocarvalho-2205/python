'''tempo = int(input('Quantos anos tem seu carro? '))
#Condição composta
if tempo <= 3:
    print('Seu carro está novo.')
else:
    print('Seu carro precisa ser trocado.')
print('Comanto fora do bloco.')


#Condição simplificada para programas simples
print('Carro novo.' if tempo<=3 else'Carro Velho')

print('fim')

nome = str(input('Digite seu nome: '))
if nome == 'Mário':
    print('Bonito nome.')
else:
    print('"Mais um."')
print(f'Muito prazer {nome}')'''
n1 = float(input('Digite a 1 nota: '))
n2 = float(input('Digite a 2 nota: '))
m = (n1 + n2) / 2
if m >= 6:
    print('Sua media foi {:.2f}, e voce foi aprovado.'.format(m))
    print('Parabens!')
else:
    print(f'Sua media foi {m:.2f}, e você não passou.')
    print('Precisa estudar mais.')
print('Nos veremos ano que vem!!')
#condição simplificada
print('Parabens \nVocê foi aprovado!!' if m>=6 else 'estude mais \nVoce não passou!')