#Exercício Python 48: Faça um programa que calcule a soma entre
# todos os números que são múltiplos de
# três e que se encontram no intervalo de 1 até 500.

soma = 0 # Variavel para a soma dos valores
cont = 0 # Variavel para a contagem da repetição

for c in range(1, 500, 2): # O inicio do loop no 1, pula uma repetição desnecessaria,
    # e com o salto de 2 para para pegar os numeros impares
    if c % 3 == 0: # divisiveis por 3
        cont += 1 # para contar se usa a variavel + 1
        soma += c # para somar, usar a variavel de soma + variavel dos dados

print('A soma dos {} numeros impares multiplos de 3 é {}'.format(cont, soma))
