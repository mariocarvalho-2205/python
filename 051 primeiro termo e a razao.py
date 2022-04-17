# 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = (primeiro + (10 - 1) * razao) + razao # fiz a formula ja incluindo a
                                               # soma da razão na variavél usando
                                               # as regras das expressões aritmeticas.

for c in range(primeiro, decimo, razao):
    print(c, end=' -> ')
print('ACABOU!')