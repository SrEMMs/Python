temp = float(input('Informe a temperatura em °C: '))

F = temp * 9 / 5 + 32
K = temp + 273

print('A temperatura de {}°C para Fahrenheit é de {:.2f}F e em Kelvin é de {:.2f}K.'.format(temp, F, K))
