jogador = dict()
gols = list()
totalGol = 0

jogador['nome'] = str(input('Nome do jogador: '))
pt = int(input(f'Quantas patidas {jogador["nome"]} jogou? '))
for i in range (0, pt):
    golPt = int(input((f'    Quantos gols na partida {i + 1}? ')))
    totalGol += golPt
    gols.append(golPt)
    jogador['gols'] = gols
    jogador['total'] = totalGol
    '''jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)'''

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {pt} partidas.')
for i in range(0, pt):
    print(f'    => Na partida {i+1}, fez {jogador["gols"][i]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')