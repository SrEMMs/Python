#Reajuste salarial com 15% 
sal = float(input('Informe o salário: R$'))

porc = (sal * 15) / 100
novosal = sal + porc

print('O salário de R${:.2f} com o aumento de 15% passa a ser de R${:.2f}'.format(sal, novosal))
