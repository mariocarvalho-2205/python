# 061 Refaça o Desafio 051, lendo o termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('-*' * 20)
print('Os 10 termode de uma PA.')
print('-*' * 20)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
# decimo = (primeiro + (10 - 1) * razao) + razao -> dessa forma foi usada a formula matematica.
c = 0
while c < 10: # Repete o laço enquanto o contador for menor que 10

    print(primeiro, end=' -> ')
    primeiro += razao # Aqui esta sendo usada a logica,
                      # somando o primeiro termo com a razão em cada laço
                      # substituindo a formula matematica.
    c += 1
print('Acabou!!!')