# 1 forma de se fazer, mais simples.
for c in range(2, 51, 2):
    print(c, end=', ')
print()

# 2 forma funciona, porem o codigo roda mais que a primeira.
for c in range(2, 50):
    if c % 2 == 0:
        print(c, end=', ')
