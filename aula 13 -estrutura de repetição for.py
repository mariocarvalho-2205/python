'''n = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
for c in range(n, f):

    for c2 in range(n, f,):
        print(c2, c)
        if c == 2:
            print(f'olha ele {c}')
        elif c == 5:
            print('soma')
    else:
        print(c)

print('Fim!')

s = 0
for c in range(0, 5):
    n = int(input('Digite um numero: '))
    s += n
print(s)

n = 'mario'
s = ''
for c in 'mario':
    print(c)
    s += c
print(f'Fim {s}!')
c = 0

for c in range(0, 5):

    for c2 in range(0, 3):
        print(c, c2)
print('Fim!')'''
import time
import emoji

for c in range(5, 0, -1):
    print(c)
    time.sleep(0.5)
print(emoji.emojize('\033[32m:fireworks::fireworks:\033[m'))
