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
for c in range(len(ficha)):
    print(f'{c:<4} {ficha[c][0]:<10} {ficha[c][2]:>8}')

while True:
    resp2 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if resp2 <= len(ficha):
        print(f'As notas da {ficha[int(resp2)][0]} são {ficha[int(resp2)][1]}')
    elif resp2 != 999:
        print('Opção invalida!!')
    if resp2 == 999:
        break
print('Finalizado com Sucesso!')

