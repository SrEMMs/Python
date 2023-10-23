primeiro =  int(input('Primeiro termo: '))
razao = int(input('Razao: '))

termo = primeiro
i = 1

while i <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    i += 1
print('FIM!')