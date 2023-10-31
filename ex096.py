def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m².')


print('Controle de Terrenos')
print('-' * 20)
largura = float(input('Largura(m): '))
comprimento = float(input('Comprimento: '))
area(largura, comprimento)
