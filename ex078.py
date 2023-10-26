valores = []
max = 0
min = 0

for i in range(0, 5):
    valores.append(int(input(f'Informe um valor para a Posição {i}: ')))
    if i == 0:
        max = valores[i]
        min = valores[i]
    elif max <= valores[i]:
        max = valores[i] 
    elif min >= valores[i]:
        min = valores[i]
print(f'Os valores digitados {valores}')
print(f'O maior número foi {max}, nas posições: ', end='')
for c, v in enumerate(valores):
    if v == max:
        print(f'{c}...', end='')
print()
print(f'O menor número foi {min}, nas posições: ', end='')
for c, v in enumerate(valores):
    if v == min:
        print(f'{c}...', end='')
