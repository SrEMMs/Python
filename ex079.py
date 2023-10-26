números = list()

while True:
    num = int(input('Digite um valor: '))
   
    if num not in números:
       números.append(num)
       print('Valor adicionado...')
    else:
       print('Valor Duplicado!')
    op = str(input('Adicionar um novo número? [S/N] ')).strip().upper()[0]
    while op not in 'SN':
        print('Tente novamente. ', end='')
        op = str(input('Adicionar um novo número? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Os valores digitado foram → {sorted(números)}')
    