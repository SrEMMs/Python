primeiro =  int(input('Primeiro termo: '))
razao = int(input('Razao: '))

termo = primeiro
i = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while i <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        i += 1
    print('PAUSA!')

    mais = int(input('Quantos termos você quer mostrar a mais? '))
print("Progressão finalizada com {} termos mostrados.".format(total))