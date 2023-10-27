pessoas = list()
cadastro = list()
cont = 0
maxPeso = 0
minPeso = 0

while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))
    pessoas.append(cadastro[:])
    cadastro.clear()
    cont += 1
    
    if cont == 1:
        maxPeso = pessoas[0][1]
        minPeso = pessoas[0][1]
    else:
        for i in pessoas:
            if i[1] > maxPeso:
                maxPeso = i[1]
            elif i[1] < minPeso:
                minPeso = i[1]
        
    op = str(input('Voce deseja continuar? [S/N] ')).strip().upper()[0]
    while op not in 'SN':
        print('Tente novamente! ')
        op = str(input('Voce deseja continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        print('Saindo do Programa!!!')
        break
#Resultado
print('=-' * 30)
print(f'Foram cadastrados {cont} pessoas')
print(f'O maior peso foi de {maxPeso:.2f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maxPeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {minPeso:.2f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == minPeso:
        print(f'[{p[0]}] ', end='')
