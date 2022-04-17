# 057 - Faça um programa que leia o sexo, mais so aceite 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente
# até ter um valor correto

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]. ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Digite a opção correta. ')
print('Acabou!')
