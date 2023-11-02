def vota(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    
    if idade < 16:
        verifica = 'Não Vota'
    elif 16 <= idade < 18 or idade >= 65:
        verifica = 'Voto Opcional'
    else:
        verifica = 'Voto Obrigatório'
    print(f'Com {idade} anos: {verifica}')

print('-=' * 30)
ano = int(input('Informe o ano em que você nasceu: '))
vota(ano)