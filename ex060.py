num = int(input('Informe um número para o calculo do fatorial: '))
i = num
fatorial = 1

print('Calculando {}!'.format(num))
while i > 0:
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ', end='')
    fatorial *= i
    i -= 1
print('{}'.format( fatorial))
