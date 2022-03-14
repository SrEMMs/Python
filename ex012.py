#Informe o preço e a porcentagem de desconto 
preco = float(input('Informe o preço do produto: '))
desconto = int(input('Informe a porcentagem de desconto: '))

desc = (preco * desconto) / 100
novopreco = preco - desc

print('O preço é de R${:.2f}, como o desconto de {}% o preço passa a ser de R${:.2f}.'.format(preco, desconto, novopreco))
