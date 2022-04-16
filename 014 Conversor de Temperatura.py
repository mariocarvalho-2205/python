unidade = input('Voce vai digitar a temperatura em qual unidade C/F? ').upper()

if unidade == 'F':
    f = float(input('Digite a temperatura em \033[33mFahrenheit\033[m: '))
    c = 5 / 9 * (f - 32)

    print('Temperatura de {:.1f}°F, correesponde a {:.1f}°C.'.format(f, c))

else: #unidade == 'C' or 'c':
    c = float(input('Digite a temperatura em \033[32mCelsius\033[m: '))
    f = 9 * c / 5 + 32
    print('Temperatura de {:.1f}°C corresponde a {:.1f}°F.'.format(c, f))


