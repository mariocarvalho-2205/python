# 061 Refaça o Desafio 051, lendo o termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('-*' * 20)
print('Os 10 termode de uma PA.')
print('-*' * 20)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
decimo = (primeiro + (10 - 1) * razao) + razao
c = 0
while c <= primeiro:
    if c < 10:
        print(primeiro, end=' -> ')
        primeiro += razao
    c += 1
print('Acabou!!!')