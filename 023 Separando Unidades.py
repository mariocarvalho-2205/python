# Usando a separação de forma matematica.
import time
n = int(input('Digite um numero de 0 a 9999: '))

u = n // 1 % 10 # Divisao inteira por 1 e o resto da divisao por 10 para achar a unidade
d = n // 10 % 10 # Divisao inteira por 10 e o resto da divisao por 10 para achar a dezena
c = n // 100 % 10 # Divisao inteira por 100 e o resto da divisao por 10 para achar a centena
m = n // 1000 % 10 # Divisao inteira por 1000 e o resto da divisao por 10 para achar o milhar

print('Analisando o numero {}'.format(n))
print('\033[32mProcessando...\033[m')
time.sleep(3)
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
# Usando a separação como string
num = str(input('Digite novamente de 0 a 9999: '))
print('Analisando o numero {}'.format(num))

print('\033[32mProcessando...\033[m')
time.sleep(3)

print('Unidade {}'.format(num[3]))
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print('Milhar: {}'.format(num[0]))