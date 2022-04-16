nome = str(input('Digite seu nome: ')).strip().split()
print('Seu nome completo é {}.'.format(' '.join(nome)))
# Sempre lembrar de usar aspa separada antes da função ' '.join()
print('Seu primeiro nome é {}.'.format(nome[0]))

# Agora usando a formatação do f antes da frase, sem usar o .format.
print(f'Seu ultimo nome é {nome[-1]}.')

# Usando a formatação .format
print('Seu ultimo nome é {}.'.format(nome[-1]))

# usando a função len para achar o ultimo nome tambem.
print('Seu ultimo nome é {}.'.format(nome[len(nome)-1]))



