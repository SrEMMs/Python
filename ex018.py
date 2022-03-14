'''n1 = float(input('Informe o cateto oposto: '))
n2 = float(input('Informe o cateto adjacente: '))

hipotenusa = (n1 ** 2 + n2 ** 2)**(1/2)

print('A hipotenusa é {:.2f}'.format(hipotenusa))'''

import math
n1 = float(input('Informe o cateto oposto: '))
n2 = float(input('Informe o cateto adjacente: '))

hipotenusa = math.hypot(n1, n2)

print('A hipotenusa é {:.2f}'.format(hipotenusa))
