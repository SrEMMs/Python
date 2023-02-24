a = int(input('Primeiro valor: '))
b = int(input('Segundo valor:' ))
c = int(input('Terceiro valor: '))

#Verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

#Verificando o maior valor
maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
