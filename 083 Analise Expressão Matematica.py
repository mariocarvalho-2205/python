'''
083 - Crie um programa onde o usuario digite uma expressão qualquer
que use parenteses.
Seu aplicativo deverá analisar se a expressão passada está com os
parenteses abertos e fechados na ordem correta.
'''
exp = str(input('Digite a expressão: '))
pilha = []
for simb in exp:                    # Verifica cada item da string
    if simb == '(':                 # Se tiver o parentese abrindo
        pilha.append('(')           # Sera adicionado na lista pilha
    elif simb == ')':               # Verifica se existe parentese fechando
        if len(pilha) > 0:          # Verifica se tiver item na lista pilha
            pilha.pop()             # Se tiver pilha estiver cheia, será removido um item
        else:
            pilha.append(')')       # para cada parentese abrindo sera removido um parentese
            break
if len(pilha) == 0:# aqui vai contar, para cada parentese fechado, foi removido um abert.
    print('Sua expressão é valida!!')
else:
    print('Sua expressão está errada!!')







'''print('A expressão está correta' if exp.count('(') == exp.count(')')
         else 'Sua expressão está errada!!')

if exp.count('(') == exp.count(')'):
    print('Sua expressão está correta!!!')
else:
    print('Sua expressão está errada!!!')'''


