# 062 Melhore o Desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disse que quer mostrar 0 termos.

print('-*' * 20)
print('Os 10 termode de uma PA.')
print('-*' * 20)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
termo = primeiro + razao # O primeiro termo recebe a soma da razao
mais = 10 # variavel começa com 10 termos para repetir o loop inicial
c = 1 # Contator
total = 0 # vai receber o valor somado da variavel mais

while mais != 0: # Enquanto a variavel MAIS for != de 0, continua.
    total += mais # A variavel recebe a soma da variavel MAIS para continuar o loop.
    while c <= total: # Enquanto o contador for menor ou igual a var total, repete o loop.
        print(termo, end=' -> ')
        termo += razao # A var TERMO e somada a var RAZAO
        c += 1 # O contador recebe o incremento de +1 em cada laço
    print('Pausa!!')
    mais = int(input('Quantos termos voce quer mostrar mais? ')) # A var MAIS recebe o valor para continuar.
print('Progressao finalizada com {} termos.'.format(total))
print('Acabou!!!')