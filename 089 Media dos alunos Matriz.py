'''
089 - Crie um programa que leia varios ficha e guarde em uma lista composta.
No final, mostre um boletim contendo a media de cada um e mpermita que o usuario
possa mostrar as nostas de cada aluno individualmente.
'''
# Correção
ficha = list()
while True:
    nome = str(input('Nome: ')).capitalize().strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if resp == 'N':
        break

print(ficha)
print('-=' * 30)
print(f'{"No":<5}{"Nome":<10}{"Media":>9}')
# Pode ser usado as duas opçoes de laço.
for c in range(len(ficha)):
    print(f'{c:<4} {ficha[c][0]:<10} {ficha[c][2]:>8}')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

print('-' * 30)
while True:
    print('-' * 30)
    resp2 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if resp2 <= len(ficha) - 1: # com o -1 no final do len ele so pega a quantidade correta.
        print(f'As notas da {ficha[resp2][0]} são {ficha[resp2][1]}')
    elif resp2 != 999:
        print('Opção invalida!!')
    if resp2 == 999:
        print('Finalizado com Sucesso!')
        break


