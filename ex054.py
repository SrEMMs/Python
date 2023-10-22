from datetime import date

atual = date.today().year

totMaior = 0
totMenor = 0
for i in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu '.format(i)))
    idade = atual - nasc
    if idade >= 18:
        totMaior += 1
    else:
        totMenor += 1
    
print('Ao todo tivemos {} pessoas MAIORES de idade.'.format(totMaior))
print('Ao todo tivemos {} pessoas MENORES de idade.'.format(totMenor))
