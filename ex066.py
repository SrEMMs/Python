cont = 0
soma = 0

while True:
    num = int(input('Digite um número [999 faz parar]: '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f'A soma dos {cont} foi de {soma}!')