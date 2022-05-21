import random
from random import randint

aleatorio = [random.randint(0, 9) for c in range(0, 5)]
modificado = str(aleatorio)[1: -1].replace(', ', ' ')
print(f'Os valores sorteados foram: {modificado}')
print(f'O maior valor sorteado foi: {max(aleatorio)}')
print(f'O menor valor sorteado foi: {min(aleatorio)}')

sorteado = (randint(0, 10), randint(0, 10), randint(0, 10),
            randint(0, 10), randint(0, 10))
print('Os numeros soteados foram: ', end=' ')
for c in sorteado:
    print(f'{c} ', end=' ')
print(f'\nO maior valor sorteado foi: {max(sorteado)}')
print(f'O menor valor sorteado foi: {min(sorteado)}')



