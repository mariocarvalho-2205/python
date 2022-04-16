#corrigido
#imc <- peso / (altura^2)
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
#print('IMC = {:.2f}'.format(imc))
print(f'Seu IMC é {imc:.1f}.')

if imc < 18.5:
    print('Você está abaixo do peso.'.format(imc))
elif imc < 25:
    print('\033[32mVocê está com o peso ideal.\033[m')
elif imc < 30:
    print('\033[33mVocê está com sobrepeso.\033[m')
elif imc < 40:
    print('\033[34mVocê está com Obesidade.\033[m')
else:
    print('\033[35mVocê está com Obesidade Mórbida.\033[m')

#if imc > 18.5 and imc < 25:
if 18.5 <= imc < 25:
    #print('Seu IMC é {:.2f} e você está abaixo do peso.'.format(imc))
    print('\033[32mSeu IMC é {:.1f}, você está com o peso ideal.\033[m'.format(imc))
#elif imc >= 25 and imc < 30:
elif 25 <= imc < 30:
    #print('\033[32mVocê está com o peso ideal.\033[m')
    print(f'\033[33mSeu IMC é {imc:.1f}, e você está com sobrepeso.\033[m')
#elif imc >= 30 and imc < 40:
elif 30 <= imc < 40:
    #print('\033[33mVocê está com sobrepeso.\033[m')
    print(f'\033[34mSeu IMC é {imc:.1f}, e você está com Obesidade.\033[m')
elif imc >= 40:
#else: pode ser usado tambem a condição else.

    #print('\033[34mVocê está com Obesidade.\033[m')
    print(f'\033[35mSeu IMC é {imc:.1f}, e você está com Obesidade Mórbida.\033[m')
else:
    #print('\033[35mVocê está com Obesidade Mórbida.\033[m')
    print('\033[36mSeu IMC é {:.1f}, e você está abaixo do peso.\033[m'.format(imc))
