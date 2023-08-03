peso = float(input('Informe seu Peso (Kg): '))
altura = float(input('Informe sua Altura (m): '))

imc = peso / (altura**2)

print('Seu IMC é de: {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO do peso!')
elif imc <= 25:
    print('Você está com o peso IDEAL!')
elif imc <= 30:
    print('Você está com SOBREPESO!')
elif imc <= 40:
    print('Você está com OBESIDADE!')
else:
    print('Você esta com OBESIDADE MÓRBIDA!')