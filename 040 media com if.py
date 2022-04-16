#corrigido!
n1 = float(input('Digite sua nota da primeira unidade: '))
n2 = float(input('Digite sua nota da segunda unidade: '))
media = (n1 + n2) / 2

# if alternativo simplificado
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(n1, n2, media))
#if media >= 5 and media < 7:
if 7 > media >= 5:
    print('Sua media foi {:.1f} e você vai para a recuperação!'.format(media))
elif media >= 7:
    print('Sua media foi {:.1f} e foi Aprovado!!'.format(media))
elif media < 5:
#pode ser usado o else para essa condição.
    print('Que pena, sua media foi {:.1f} e você foi Reprovado!'.format(media))
