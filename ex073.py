times = ('Botafogo', 'RB Bragantino', 'Flamengo', 'Palmeiras', 'Athletico-PR', 'Grêmio', 'Atlético-MG',
         'Fortaleza', 'Fluminense', 'São Paulo', 'Cuiabá', 'Internacional', 'Bahia', 'Cruzeiro', 'Corinthians',
         'Goiás', 'Vasco da Gama', 'Santos', 'Coritiba', 'América-MG')
print('-=' * 15)
for i in times:
    print(i)
print('-=' * 15)
print(f'Os 5 primeiros time são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Botafogo está na {times.index("Botafogo") + 1}ª posição')