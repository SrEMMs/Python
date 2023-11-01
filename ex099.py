from time import sleep

def maior(* num):
    cont = 0
    maiorNum = 0
    print('-=' * 30)
    print('Analisando os valores')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maiorNum = valor
        else:
            if valor > maiorNum:
                maiorNum = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'o Maior valor informado foi {maiorNum}.')


#Programa Principal    
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()