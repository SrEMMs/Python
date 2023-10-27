matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaTerColuna = 0
somaPar = 0
maiorValorLinha2 = 0
'''Comentários são resposta do curso'''
for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha][coluna] = num
        if num % 2 == 0:
            somaPar += num
        if coluna == 2:
            somaTerColuna += num
    if linha == 0:
        maiorValorLinha2 = num
    if linha == 1 and maiorValorLinha2 < num:
        maiorValorLinha2 = num
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        '''if matriz[linha][coluna] % 2 ==0:
            somaPar += matriz[linha][coluna]'''
    print()
print('-=' * 30)
'''for linha in range(0, 3):
    somaTerColuna += matriz[linha][2]'''
print(f'Os valores somados da Terceira coluna são de: {somaTerColuna}')
print(f'A soma dos pares é de: {somaPar}')
'''for coluna in range(0, 3):
    if coluna == 0:
        maiorValorLinha2 = matriz[1][coluna]
    elif matriz[1][coluna] > maiorValorLinha2:
        maiorValorLinha2 = matriz[1][coluna]'''
print(f'O maior valor da linha 2: {maiorValorLinha2}')
print('-=' * 30)