masc = 0
fem = 0
maiorIdade = 0
sexo = ' '
op = 'S'

while True:
    if op == 'N':
        print('Saindo do Programa!')
        break
    elif op == 'S':
        print('Cadastro de Pessoas')
        idade = int(input('Informe sua idade: '))
        '''while sexo not in 'MF' 
            sexo = str(input('Informe o sexo [F/M]: ')).strip().upper()[0] Soluão da aula'''
        sexo = str(input('Informe o sexo [F/M]: ')).strip().upper()[0]
        if sexo == 'M' or 'F':
            if idade >= 18:
                maiorIdade += 1
            if sexo == 'M':
                masc += 1
            elif sexo == 'F' and idade < 20:
                fem += 1
        else:
            print('Opção Inválida!')
            sexo = str(input('Escolha uma opção válida [M/F]: '))
    else:
        print('Opção Inválida!')
    op = str(input('Você quer continuar: ')).strip().upper()[0]

if maiorIdade == 1:
    print('Temos apenas 1 pessoa com mais de 18 anos cadrastrado!')
elif maiorIdade == 0:
    print('Não temos pessoas com 18 anos cadastrados!')
else:
    print(f'Total de pessoas com mais de 18 anos: {maiorIdade}')

if masc == 1:
    print('Temos apenas 1 Homem cadastrado!')
elif masc == 0:
    print('Não temos homens cadastrados!')
else:
    print(f'Temos ao todo {masc} homens cadastrados')
    
if fem == 1:
    print('Temos apenas 1 mulher com menos de 20 anos no cadastro!')
elif fem == 0:
    print('Não temos mulheres com menos de 20 anos cadastradas!')
else:
    print(f'E temos {fem} mulheres com menos de 20 anos')
