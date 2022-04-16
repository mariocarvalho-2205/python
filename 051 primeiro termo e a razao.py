# 051 - Progressão AritmeticaDesenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro = int(input('Primeiro elemento: '))
razao = int(input('Razão: '))
#n = int(input('Quantos elementos: '))
decimo = primeiro + (10 - 1) * razao
#ultimo = primeiro + (n - 1) * razao
#ultimo += 1
#for var in range(primeiro, ultimo, razao):
for c in range(primeiro, decimo + razao, razao):
    print(c, end=' -> ')
print('ACABOU!')