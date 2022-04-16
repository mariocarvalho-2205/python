# \n - serve para quebrar linha do texto
#Fatiamento de String - no fatiamento, a contagem do indice sempre começará pelo numero 0
frase = 'minha primeira nome será feita assim'
frase2 = '   Minha seguna nome ESTÁ dessa forma e ficará diferente.   '
frase3 = 'testando split e a função join'
print(frase[7]) #imprime somente a letra de posição informada
print(frase[9:13])
''' imprime um trecho da nome 9:13 representa o inicio e o fim
sendo que a ultima posição não será impressa.'''
print(frase[9:21])
'''se o ultimo numero for maior que o ultimo indice, 
será impresso até o final da nome'''
print(frase[6:21:2]) # o ultimo numero representa
print(frase[:5]) #imprime do inicio até a posição informada
print(frase[5:]) #imprime do indice informado até o final da nome
print(frase[3::3]) #Significa que imprime do indice informado até o final com um salto de 3 em 3
print(frase[::2])#imprime do inicio ao final com salto de 2 em 2

#Analise de String
# Função len - mostra o comprimento da string
print(len(frase))

# Função count - Serve para contar a quantidade de uma letra ('string')
# tem diferença entre maiuscula e minuscula
print(frase.count('i'))
print('string (i) com fatiamento', frase.count('i', 0, 10))
''''#conta as strings informadas usando fatiamento, 
# usa a mesma regra, porem separando com virgula'''

#Função find - indica onde começa o trecho selecionado aparece
print('Trecho (pri) começa na {} posição do indice.'.format(frase.find('pri')))
print(frase.find('joao')) #serve tambem para verificar se o trecho existe na string e mostra -1

#Operador in - verifica se existe o trecho na nome, retornando falso ou verdadeiro
print('minha' in frase)#Verifica se existe o trecho na nome, retornando falso ou verdadeiro
print('joao' in frase)

#Função replace - verifica se existe a palavra e substitui por outra
print(frase.replace('minha', 'sua'))
print(frase.replace('s','*'))
#Função upper() - muda a letra ou string por maiuscula
print(frase.upper())
#Função lower() - muda para string para minuscula
print(frase.lower())
#Função capitalize() - deixa somente o primeiro caractere maiusculo
print(frase.capitalize())
#Função title() - muda o primeiro caractere de todas as palavras para maiusculo
print(frase.title())
#Função strip() - remove os espaços desnecessarios no inicio e no final da string
print(frase2)
print(frase2.strip())
#Função rstrip() - Remove somente os espaços desnecessarios da direita
print(frase2.rstrip())
#Função lstrip() - Remove somente os espaços desnecessarios da esquerda
print(frase2.lstrip())
#Função split() - divide a nome separando cada palavra e criando novas cadeias de caracteres
#recomeçando a contagem do indice em cada palavra recebando uma indexação nova,
#criando uma lista, na qual cada palavra terá uma numeração
print(frase3.split())
listafrase2 = frase2.split() #Variavel recebe a variavel splitada e cria uma lista
print(listafrase2)
print(listafrase2[3]) # exibe a string splitada na lista
print(listafrase2[3][2]) # exibe a string splitada na lista e mostra o indice da string

#Função join() - faz a junção dos nomes separados em lista com string ou espaço
print(''.join(frase3))

print('''eu digito um texo grande quebrando a linha
sem precisar fazer mais nada
 do jeito que estou digitando''')
#podemos unificar as funçoes
#ex: print(nome.upper().count('O') - dessa forma ele converte a letra o
# minuscula em maiuscula e faz a contagem
print(frase, ' letra s ', frase.upper().count('S'), ' vezes')
