nome = str(input('Digite seu nome completo: ')).strip()

# Tem que colocar o verificador para minuscula
print('Tem \033[36mSilva\033[m no nome? {}'.format('silva' in nome.lower()))

# Tem que colocar o verificador para minuscula
print('Tem \033[36mSilva\033[m no nome? {}'.format('SILVA' in nome.upper()))