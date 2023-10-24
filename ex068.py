from random import randint

vit = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!!!')
            vit +=1
        else:
            print('Você Perdeu!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!!!')
            vit +=1
        else:
            print('Você Perdeu!!!')
            break
    print('Vamos jogar denovo!!!')
if vit == 1:
    print(f'Fim de Jogo! Você venceu {vit} vez.')
elif vit == 0:
    print('Que pena! Você não venceu nem uma vez.')
else:    
    print(f'Fim de Jogo! Você venceu {vit} vezes.')