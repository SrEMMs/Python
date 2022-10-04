num_int = input('Digite um numero interio: ')
"""par_impar = num_int.isnumeric() % 2

print('{}'.format(par_impar))

if num_int.isnumeric() and par_impar == 0:
    print('PAR')
elif num_int.isnumeric() and par_impar != 0:
    print('IMPAR')
else:
    print('ERRO')"""

if num_int.isnumeric() == 0:
    print('ERRO')
else:
    par_impar = int(num_int)
    res = par_impar % 2
    if res == 0:
        print('PAR')
    else:
        print('IMPAR')
