# 055 Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0 # A variavel recebe valor zero.
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o {} pessoa: '.format(i))) # Aqui faz a leitura do primeiro laço.
    if i == 1: # Aqui verifica se o primeiro laço é igual a 1
        maior = peso # Sendo igual a 1, ele atribui o valor as duas variaveis
        menor = peso # maior e menor
    else: # no segundo laço, começa a atribuir o valor da variavel peso as variaveis maior e menor.
        if peso > maior:  # nesses dois if, atribui-se os valores maiores e menores
            maior = peso  # as suas variaveis maior e menor
        if peso < menor:
            menor = peso
print('O maior peso lido foi {:.1f}Kg. '.format(maior))
print('O menor peso lido foi {:.1f}Kg. '.format(menor))

