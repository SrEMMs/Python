import imp
from random import randint

computador = randint(0,5) #Sorteia um número de 0 a 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador coloca um valor

if jogador == computador:
    print('PARABÉNS! Você ganhou!!!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
