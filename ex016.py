#O programa irá ler um número Real e mostrar a apenas a poeção inteira
"""num = float(input('Digite um número: '))

porcint = num // 1

print('O valor digitado foi {} e sua porção inteira é {:.0f}.'.format(num, porcint))"""

"""from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, trunc(num)))"""

num = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {:.0f}.'.format(num, int(num)))
