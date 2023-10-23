cont = 0
total = 0
num = int(input('Digite um número [999 para finalizar]: '))
while num != 999:
    total += num
    cont += 1        
    num = int(input('Digite um número [999 para finalizar]: '))
print('Você digitou {} números e sua soma é de {}'.format(cont, total))
    