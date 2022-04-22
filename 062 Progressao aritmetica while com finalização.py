# 062 Melhore o Desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disse que quer mostrar 0 termos.

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