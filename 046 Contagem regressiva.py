import time
import emoji
print('*' * 45)
print('Preparem-se para a contagem para os fogos!!!')
print('*' * 45)
for c in range(10, -1, -1): # conceito - range(inicio, fim, salto)
    print(c)
    time.sleep(0.5)
print(emoji.emojize('\033[32m:fireworks:\033[m' * 10))
