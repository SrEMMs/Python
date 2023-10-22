maior = 0
menor = 0

for i  in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O Maior peso lido foi de {}Kg'.format(maior))
print('O Menor peso lido foi de {}Kg'.format(menor))
