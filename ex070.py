prodBarato = ' '
precoBarato = 0
totalCompra = 0
cont1000 = 0
op = 'S'

print('-*'*30, end='-')
print('\n{:^40}'.format('Loja do Seu Zé'))
print('-*'*30, end='-')
print('\n')
while True:
    if op == 'N':
        print('Saindo do programa!')
        break
    elif op == 'S':
        nomeProduto = str(input('Nome do Produto: '))
        preco = float(input('Preço do Produto: R$'))
        
        totalCompra += preco
        
        if preco >= 1000:
            cont1000 += 1
            
        if precoBarato == 0:
            prodBarato = nomeProduto
            precoBarato = preco
        elif precoBarato > preco:
            prodBarato = nomeProduto
            precoBarato = preco
        op = str(input('Você deseja continuar [S/N]: ')).strip().upper()[0]
        while op not in 'SN':
            op = str(input('Você deseja continuar [S/N]: ')).strip().upper()[0]
print(f'O total da compra foi R${totalCompra:.2f}')
print(f'Temos {cont1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prodBarato} que custa R${precoBarato:.2f}')