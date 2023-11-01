from random import randint 
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num} ', end='')
        sleep(0.5)
    print('Pronto!')

def somaPar(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}')


#Programa Principal
numeros = list()
sorteia(numeros)
somaPar(numeros)