''' 077 Crie um programa que tenha uma tupla com varias palavras
(não usar acentos). Depois disso você deve mostrar para cada palavra quais são suas
vogais
'''

palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado','programador', 'futuro')
cont = 0
for c in range(len(palavras)):
    print(f'\nNa palavra {str(palavras[c]).upper()} temos ', end=' ')
    for vogal in palavras[cont]:
        if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':
            print(f'{vogal}', end=' ')
    cont += 1
# Correção:
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou': # Se quiser pegar os acentos tem que colocar na string do if 'aáãâ'
            print(letra, end=' ')