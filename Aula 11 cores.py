print('\033[1;31;43mOlá Mundo\033[m')
print('\033[0;30;41mOlá, Mundo\033[m')
'''Maneira 1: Código ANSI para cor no python
('\033[style; text; backgroundtexto aqui[m')
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Padrão de cores ANSI.
Este são os códigos de estilo e cor que melhor funcionam no Python.
Sintaxe: ``\033[ESTILO;FG;BGm``.
O texto deve ser inserido apos a letra ``m``.
Estilo:
- **0**: (Nome) sem cor.
- **1**: (old) Negrito.
- **4**: (Underline) Sublinhado.
- **7**: (Negative) Inverte letra e fundo.
Cor do texto (fg):
- **30**: Branco.
- **31**: Vermelho.
- **32**: Verde.
- **33**: Amarelo.
- **34**: Azul.
- **35**: Magenta.
- **36**: Cyan (azul claro).
- **37**: Cinza.
Cor de fundo (bg):
- **40**: Branco.
- **41**: Vermelho.
- **42**: Verde.
- **43**: Amarelo.
- **44**: Azul.
- **45**: Magenta.
- **46**: Cyan (azul claro).
- **47**: Cinza.
    **OBS**: Para limpar/limitar a formatação deve-se utilizar ``\033[m``
"""

estilo = {'none': 0, 'negrito': 1, 'sublinhado': 4, 'inverter': 7}

fg = {'branco': 30, 'vermelho': 31, 'verde': 32, 'amarelo': 33,
      'azul': 34, 'magenta': 35, 'cyan': 36, 'cinza': 37}

bg = {'branco': 40, 'vermelho': 41, 'verde': 42, 'amarelo': 43,
      'azul': 44, 'magenta': 45, 'cyan': 46, 'cinza': 47}

cores = {'limpa':'\033[m', 'azul':'\033[34m', 'verde':'\033[32m', 'vermelho':'\033[31m'}

if __name__ == '__main__':
    print('Estilo')
    print(f"\033[{estilo['none']}m Texto normal.")
    print(f"\033[{estilo['negrito']}m Texto em negrito.")
    print(f"\033[{estilo['sublinhado']}m Texto sublinhado.")
    print(f"\033[{estilo['inverter']}m Texto com fg e bg invertidos.\n\033[m")

    print('Cor da fonte')
    print('\033[0;30m Branco.')
    print('\033[0;31m Vermelho.')
    print('\033[0;32m Verde.')
    print('\033[0;33m Amarelo.')
    print('\033[0;34m Azul.')
    print('\033[0;35m Magenta.')
    print('\033[0;36m Cyan.')
    print('\033[0;37m Cinza.\n\033[m')

    print('Cor de fundo')
    print('\033[0;40m Branco.')
    print('\033[0;41m Vermelho.')
    print('\033[0;42m Verde.')
    print('\033[0;43m Amarelo.')
    print('\033[0;44m Azul.')
    print('\033[0;45m Magenta.')
    print('\033[0;46m Cyan.')
    print('\033[0;47m Cinza.\n\033[m')

print('{}Olá, Mundo{}'.format('\033[4;34m', '\033[m'))