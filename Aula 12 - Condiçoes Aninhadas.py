import emoji
nome = str(input('Digite um nome: ')).capitalize()

if nome == 'Mario': # Condição simples é quando usamos somente o if.
    print('\033[32mSeu nome e muito bonito!\033[m ')
elif nome == 'Joao' or nome == 'Maria' or nome == 'Antonio':
    # Condição aninhada é quando usamos elif dentro do if, e pode ser usado varias vezes.
    print('\033[33mSeu nome e bastante popular!\033[m')
elif nome == 'Adilma':
    print(emoji.emojize('\033[31mSeu nome e diferente e bonito!!\033[m:red_heart:'))
else: # Condição composta é quando usamos o else.
    print('\033[34mSeu nome e bastante comum!\033[m')
print('Prazer em conhecer-lo \033[35m{}\033[m!'.format(nome))