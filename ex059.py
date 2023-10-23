n1 = int(input('Informe o Primeiro número: '))
n2 = int(input('Informe o Segundo número: '))

opcao = 0

while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa
    ''')
    opcao = int(input('Selecione uma opção: '))
    
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O primeiro número é maior! {} > {}'.format(n1, n2))
        elif n2 > n1:
            print('O segundo número é maior! {} > {}'.format(n2, n1))
        else:
            print('Os números são iguais!!')
    elif opcao == 4:
        n1 = int(input('Informe um novo número: '))
        n2 = int(input('Informe um novo número: '))
    else:
        print('Opção Inválida!!')
print('Saindo!!!')