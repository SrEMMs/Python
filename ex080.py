valores = []

for i in range(0, 5):
    num = int(input('Informe um valor: '))
    if i == 0 or num > valores[len(valores)-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adiconado na posição {pos} da lista')
                break
            pos += 1

print(f'Os valores digitados em ordem crescente foram {valores}')