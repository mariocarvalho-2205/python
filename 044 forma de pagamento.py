#CORRIGIDO
print('{:=^40}'.format(' LOJAS CARVALHO '))
produto = float(input('Digite o preço das compras: R$ '))
print('''Qual a forma de pagamento?
[ 1 ] = A vista no dinheiro/cheque: 10% de desconto.
[ 2 ] = A vista no cartão: 5% de desconto.
[ 3 ] = 2 vezes no cartão: Valor normal
[ 4 ] = 3 ou mais vezes: Tem 20% de acrescimo.''')
pag = int(input('Escolha uma das opções acima: '))
if pag == 1:
    preco = produto - (produto * 10 / 100)
    #print(f'Você teve 10% de desconto e irá pagar R$ {preco:.2f}')
elif pag == 2:
    preco = produto - (produto * 0.05)
    #print(f'Você teve 5% de desconto e ira pagar R$ {preco:.2f}')
elif pag == 3:
    preco = produto
    parcela = preco / 2
    print(f'Sua compra será percelado em 2 vezes de R$ {parcela:.2f} SEM JUROS!')
elif pag == 4:
    preco = produto + (produto * 20 / 100)
    totparc = int(input('Quantas parcelas você vai dividir? '))
    parcela = preco / totparc
    print(f'Sua compra será parcelada em {totparc} vezes de R$ {parcela:.2f} COM JUROS!')
else:
    preco = produto
    print('Opção invalida de pagamento!')
print('Sua compra de R$ {:.2f}, vai custar R$ {:.2f} no final.'.format(produto, preco))
