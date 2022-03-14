import imp
import nturl2path


import random
n1 = input('Informe o 1 nome: ')
n2 = input('Informe o 2 nome: ')
n3 = input('Informe o 3 nome: ')
n4 = input('Informe o 4 nome: ')

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print('O escolhido foi o/a {}.'.format(escolhido))
