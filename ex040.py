nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

if 7 > media >= 5:
    print("Sua média é de {} e você está de RECUPERAÇÃO!".format(media))
elif media < 5:
    print("Sua média é de {} e você foi REPROVADO!".format(media))
else:
    print("Sua média é de {} e você foi APROVADO!".format(media))