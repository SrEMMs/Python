valores = []
cont = 0

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    cont += 1
    op = str(input('Você quer continuar: [S/N] ')).strip().upper()[0]
    while op not in 'SN':
        print('Opç~]ao inválida! Tente novamente.')
        op = str(input('Você quer continuar: [S/N] ')).strip().upper()[0]
    if op == 'N':
        print('Saindo do Programa!!!')
        break
print('=-' * 30)
print(f'Foram digitados {cont} números')
valores.sort(reverse=True)
print(f'Os números em forma Decrescente: {valores}')
if 5 not in valores:
    print('O valor 5 não foi digitado!')
else:
    print('O valor 5 foi digitado na lista!')
