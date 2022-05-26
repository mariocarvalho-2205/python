'''
083 - Crie um programa onde o usuario digite uma expressão qualquer
que use parenteses.
Seu aplicativo deverá analisar se a expressão passada está com os
parenteses abertos o fechados na ordem correta.
'''
exp = str(input('Digite a expressão: '))
print('A expressão está correta' if exp.count('(') == exp.count(')')
         else 'Sua expressão está errada!!')

if exp.count('(') == exp.count(')'):
    print('Sua expressão está correta!!!')
else:
    print('Sua expressão está errada!!!')