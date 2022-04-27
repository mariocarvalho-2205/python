print('-*' * 20)
print('-' * 12, 'Tabuada V4.0:', '-' * 12)
print('-*' * 20)

while True:
    print('-' * 40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    op = str(input('''Qual operador voce quer usar? 
[+]Somar 
[-]Subtrair 
[*]Multiplicar 
[/]Dividir: ''')).upper().strip()
    print('-' * 40)
    c = 1
    while c <= 10:
        if op == '+':
            print(f'{n:2} + {c:2} = {n + c:2}')
        elif op == '-':
            print(f'{c + (n - 1):2}  - {n:2} = {c - 1:2}')
        elif op == '*':
            print(f'{n:2}  x {c:2} = {n * c:2}')
        elif op == '/':
            if n > 0:
                print(f'{n * c:2}  / {n:2}  = {(n * c) / n:.0f}')
            else:
                print('Zero não é divisivel:')
                break
        c += 1
print('O programa encerrou porque foi digitado um valor negativo.')

