cont = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
        'dezoito', 'dezenove', 'vinte')
op = 'S'

while True:
    if op == 'N':
        print('Saindo do Programa!!!')
        break
    elif op == 'S':
        while True:
            num = int(input('Digite um número entre 0 e 20: '))
            if 0 <= num <= 20:
                break    
            print('Tente novamente. ', end='')

    print(f'Você digitou o número {cont[num]}')
    
    op = str(input('Você deseja continuar [S/N]: ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Você deseja continuar [S/N]: ')).strip().upper()[0]

