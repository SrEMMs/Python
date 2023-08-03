from datetime import date

ano = int(input("Informe o ano de nascimento: "))

anoAtual = date.today().year
idade = anoAtual - ano

print("O atleta tem {} anos.".format(idade))
if idade < 10:
    print("Você é categoria MIRIM")
elif 15 > idade > 9:
    print("Você é categoria INFANTIL")
elif 20 > idade > 14:
    print("Você é categoria JÚNIOR")
elif 26 > idade > 19:
    print("Você é categoria SÊNIOR")
else:
    print("Você é categoria MASTER")

