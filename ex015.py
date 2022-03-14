#Aluguel de um veiculo sendo R$60,00 dia e R$0,15 por Km
Km = float(input('Informe quanto Km foram percoridos: '))
dias = int(input('E os dias alugados: '))

paluguel = (dias * 60) + (Km * 0.15)

print('Você irá pagar R${:.2f} pelo aluguel do carro.'.format(paluguel))
