primeiro =  int(input('Primeiro termo: '))
razao = int(input('Razao: '))

decimoTermo = primeiro + (10 - 1) * razao

for i in range(primeiro, decimoTermo + razao, razao):
    print('{} '.format(i), end='→ ')
print('FIM!')