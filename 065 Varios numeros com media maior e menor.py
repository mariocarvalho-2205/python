# 065 Crie um programa que leia varios numeros inteiros pelo teclado.
# No final da execução, mostre a media entre todos os valores e qual foi
# o maior e o menor valor lido. O programa deve perguntar ao usuario se ele quer
# continuar a digitar valores.
total = maior = menor = cont = 0
continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um numero: '))
    total += num
    cont += 1
    if cont == 1: # Sempre que o contador for igual a 1, prosegue a condicional
        maior = menor = num # atribuindo valor da variavel num as variaveis maior e menor.
    else: # Aqui verifica a condicional de maior e menor
        if num > maior:
            maior = num # Aqui é atribuido valor se var-num for maior.
        if num < menor:
            menor = num # Aqui é atribuido valor se var-num for menor.
    continuar = str(input('Quer continuar [S/N]? ')).strip().upper() # A validação tem que estar
        # dentro do laço while.
media = total / cont
print('Foram digitados {} numeros, e a media entre eles é {:.2f}'.format(cont, media))
print('Dos numeros digitados, o maior foi {}, e o menor foi {}.'.format(maior, menor))
print('Fim!!!')