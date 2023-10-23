num = int(input('Quantos termos você deseja mostrar? '))
i = 3

t1 = 0
t2 = 1

print('{} → {}'.format(t1, t2), end='')

while i <= num:
    total = t1 + t2
    print(' → {}'.format(total), end='')
    t1 = t2
    t2 = total 
    i += 1
print(' → FIM!')