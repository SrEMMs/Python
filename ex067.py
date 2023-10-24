i = 0

while True:
    num = int(input('Informe um número para ver sua tabuada! '))
    if num < 0:
        print('Saindo!!!')
        break
    else:
        print(f'-----Tabuada de {num}-----')
        for i in range(1, 11):
            print(f'{num} x {i} = {num * i}')
        print('-' * 20)
