from random import randint

comp = randint(0, 10)
cont = 1

jogador = int(input('Tente advinhar um número de 0 a 10: '))

while jogador != comp:
    cont += 1
    if comp > jogador:
        print('Mais... ', end='')
    else:
        print('Menos... ', end='')
    
    jogador = int(input('Tente novamente: '))

print('Parabens! Você acertou com {} tentativas.'.format(cont))