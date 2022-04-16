import math

ang = float(input('Digite um angulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O seno do angulo {:.1f} é {:.2f}'.format(ang, seno))
print('O Coseno do angulo {:.1f} é {:.2f}'.format(ang, cosseno))
print('A Tangente do angulo {:.1f} é {:.2f}'.format(ang, tangente))

from math import radians, tan, sin, cos

ang = float(input('Digite um angulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O seno do angulo {:.1f} é {:.2f}'.format(ang, seno))
print('O Coseno do angulo {:.1f} é {:.2f}'.format(ang, cosseno))
print('A \033[32;33mTangente\033[m do angulo {:.1f} é {:.2f}'.format(ang, tangente))