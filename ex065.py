cont = 0
maior = 0
menor = 0
media = 0
op = 'S'

while op not in 'N':
    if op == 'S':
        num = int(input('Digite um número: '))
        op = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]
        if cont == 0:
            maior = num
            menor = num  
        else:
            if num > maior:
                maior = num
            elif num < menor:
                menor = num
        media += num
        cont += 1
    else:
        print('Opção inválida!')
        op = 'S'
print('Você digitou {} números e sua média é de {}'.format(cont, media / cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))