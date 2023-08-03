print('-='*13)
print('Analisador de Triângulos')
print('-='*13)
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
print('-='*13)

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima PODEM FORMAR um Triângulo! ', end='')
    if seg1 == seg2 == seg3:
        print('EQUILÁTERO!')
    elif seg1 != seg2 != seg3 != seg1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um Triângulo!')
