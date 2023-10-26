lista = []
listaPares = []
listaImpares = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    
    if num % 2 == 0:
        listaPares.append(num)
    else:
        listaImpares.append(num)    
    
    op = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    while op not in 'SN':
        print('Tente novamente! ')
        op = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        print('Saindo do programa!')
        break
''' Resolução aula
for i, v in enumerate(lista):
    if v @ 2 == 0:
        listaPares.append(v)
    else:
        listaImpares.append(v)'''    
print('=' * 30)
listaPares.sort()
listaImpares.sort()
print(f'Lista completa: {lista}')
print(f'Lista de Pares: {listaPares}')
print(f'Lista Ímpares: {listaImpares}')
