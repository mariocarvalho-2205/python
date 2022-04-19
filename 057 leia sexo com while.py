# 057 - Faça um programa que leia o sexo, mais so aceite 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente
# até ter um valor correto


sexo = str(input('Digite o sexo [M/F]. ')).upper().strip()[0] # .upper para maiuscula,
                                                                  # strip para remover espaços
                                                                  # [0] para pegar so a primeira letras
                                                                  # usando fatiamento.
while sexo not in 'MmFf': # dessa forma a variavel já é validada.
    sexo = str(input('Dados invalidos. Por favor digite o sexo [M/F]. ')).upper().strip()[0]

print('Sexo {} digitado com sucesso. '.format(sexo))





'''sexo = 
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]. ')).upper().strip()[0] # .upper para maiuscula,
                                                                  # strip para remover espaços
                                                                  # [0] para pegar so a primeira letras
                                                                  # usando fatiamento.
    if sexo == 'M':
        print('Sexo Masculino digitado com sucesso. ')
    elif sexo == 'F':
        print('Sexo Feminino digitado com sucesso. ')
    #elif sexo != 'M' and sexo != 'F':
    else:
        print('Dados invalidos. Por favor, informe seu sexo. ')

print('Acabou!')'''
