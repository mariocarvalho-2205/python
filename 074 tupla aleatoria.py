import random
#aleatorio = []

aleatorio = [random.randint(0, 9) for c in range(0, 5)]
#for c in range(0, 5):
    #aleatorio.append(random.randint(0, 9))
modificado = str(aleatorio)[1: -1].replace(', ', ' ')

print(f'Os valores sorteados foram: {modificado}')
print(f'O maior valor sorteado foi: {max(aleatorio)}')
print(f'O menor valor sorteado foi: {min(aleatorio)}')
