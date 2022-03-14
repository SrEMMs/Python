#Reajuste salarial com 15% 
sal = float(input('Informe o salário: R$'))

novosal = (sal * 85) / 100

print('O salário de R${:.2f} com o desconto passa a ser de R${:.2f}'.format(sal, novosal))
