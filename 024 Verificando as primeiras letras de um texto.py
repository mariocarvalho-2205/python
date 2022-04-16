# .strip() no final da leitura da string para remover espaços do inicio e do final.
cidade = str(input('\033[31mEm que cidade você nasceu:\033[m ')).strip()


# Converter tudo para maiuscula para reconhecer independente da forma digitada.
print(cidade[:5].upper() == 'SANTO') #Usa o fatiamento para verificar se tem o nome.
