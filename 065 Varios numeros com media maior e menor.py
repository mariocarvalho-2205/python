# 065 Crie um programa que leia varios numeros inteiros pelo teclado.
# No final da execução, mostre a media entre todos os valores e qual foi
# o maior e o menor valor lido. O programa deve perguntar ao usuario se ele quer
# continuar a digitar valores.
total = 0
maior = 0
menor = 0
cont = 0

continuar = True


while continuar == True:
    num = int(input('Digite um numero: '))
    total += num
    maior = num
    menor = num
    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    else:
        if continuar == 'S':
            continuar = True
    cont += 1
media = total / cont
print('Foram digitados {} numeros, e a media entre eles é {}'.format(cont, media))
print('Dos numeros digitados, o maior foi {}, e o menor foi {}.'.format(maior, menor))
print('Fim!!!')