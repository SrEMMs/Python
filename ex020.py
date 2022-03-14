import random
n1 = input('Informe o 1 nome: ')
n2 = input('Informe o 2 nome: ')
n3 = input('Informe o 3 nome: ')
n4 = input('Informe o 4 nome: ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem será ')
print(lista)
