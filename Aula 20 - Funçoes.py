'''
Aula 20- Funções
Funções são rotinas que serao executadas repetidamente no decorrer do codigo.
E poderam conter parametros dentro dos parenteses.
'''

#  Criando uma mensagem personalizada.

def mensagem(msg):  # mensagem(pose ser usado parametro aqui dentro) e o titulo da função.
    # Para chamar a função e so digitar o titulo seguido de (com o parametro aqui dentro)
    print('-=' * 15)
    print(f'{msg:^30}')
    print('-=' * 15)

#frase = str(input('Digite uma mensagem: ')).upper()
#mensagem(f'{frase}')
mensagem('Minha Vida se chama ADY!!!')

#  Função para somar parametros
a = 5
b = 7
c = a + b

#a = int(input('Digite o primeiro valor: '))
#b = int(input('Digite o segundo valor: '))
def soma(a, b):
    s = a + b
    print(f'a = {a}, b = {b} Somando tudo fica {s:>3}')
#soma(a, b)
soma(a = 2, b = 6)
soma(b = 17, a = 20)


# Empacotar parametros.

def contador(* num):  # mostrando os valores
    for valor in num:
        print(f'{valor}', end=' ')
    print('FIM!!')

def contador2(* num):  # contando os valores da função
    tam = len(num)
    print(f'recebi os valores {num} e sao ao todo {tam} numeros')


contador(1, 2, 6)
contador(4, 5, 6, 7, 9, 10)
contador(2, 4)
contador2(1, 2, 6)
contador2(4, 5, 6, 7, 9, 10)
contador2(2, 4)

# Dobrando valores com função

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(f'A dobra dos valores é {valores}')

# Desempacotar
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)
