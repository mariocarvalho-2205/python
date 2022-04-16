preco = float(input('Digite o preço do produto R$ '))

desconto = 0.05

print('de R$ {}{:.2f}{}, o produto ficara por R$ {:.2f} com 5% de desconto'.format('\033[36m', preco, '\033[m', preco-(preco*desconto)))