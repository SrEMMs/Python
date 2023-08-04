preco = float(input('Informe o preço das compras: R$ '))

print('FORMAS DE PAGAMENTO\n[1] À vista dinheiro\n[2] À vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
op = int(input('Escolha uma opção: '))

if op == 1:
    print('Sua compra foi de R${:.2f}, você terá um desconto de 10%!'.format(preco))
    print('Você irá pagar R${:.2f}!'.format((preco*90)/100))
elif op == 2:
    print('Sua compra foi de R${:.2f}, você terá um desconto de 5%!'.format(preco))
    print('Você irá pagar R${:.2f}!'.format((preco*95)/100))
elif op == 3:
    print('Sua compra foi de R${:.2f}, você não terá desconto!'.format(preco))
    print('Você irá pagar 2 parcelas de R${:.2f}!'.format(preco/2))
elif op == 4:
    parcelas = int(input('Quantas parcelas: '))
    print('Sua compra foi de R${:.2f}, você não terá um acréscimo de 20%!'.format(preco))
    juros = (preco * 120) / 100
    print('Você irá pagar R${:.2f} em {} parcelas de R${:.2f}!'.format(juros, parcelas, juros/parcelas))
