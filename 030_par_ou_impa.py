num = int(input('Digite um numero: '))
#resultado = num % 2 >>> Usando variavel para armazenar o resultado

#condição composta
# if resultado == 0: usando a variavel para fazer a condição
if num % 2 == 0: # Fazendo o calculo na propria condição
    print('O numero é par.')
else:
    print('O numero e impar.')

#condição simples
print(f'O numero {num} é par.' if num % 2 == 0 else f'O numero {num} é impar.')

