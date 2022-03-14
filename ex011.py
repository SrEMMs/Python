#Ler base e altura e ver quantos litros de tinta serão necessáios para pintar a mesma(sendo 1l por 2m²)
largura = float(input('Informe a LARGURA da parede (em metros): '))
altura = float(input('Informe a ALTURA da parede (em metros): '))

area = largura * altura
tinta = area / 2

print('A área da parede é de {:.2f}m².'.format(area))
print('Será necessário {} litros de tinta para pintar toda a parede.'.format(tinta))
