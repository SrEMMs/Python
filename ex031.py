distancia = float(input('Qual a distancia da sua viagem? '))
print('Você está prestes a comceçar uma viagem de {}Km.'.format(distancia))

preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print('E o preço da dua passagem será de R${:.2f}'.format(preco))