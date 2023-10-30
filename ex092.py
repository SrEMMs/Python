from datetime import date
data = date.today().year

cadastro = dict()

cadastro['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
idade = data - ano
cadastro['idade'] = idade
cadastro['ctps'] = int(input('Carteira de Trabalho [0 não tem]: '))
if cadastro['ctps'] > 0:
    cadastro['anoContratacao'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['anoContratacao'] + 35) - data)

print('-=' * 30)
for k, v in cadastro.items():
    print(f'    - {k} é igual a {v}')
