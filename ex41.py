# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# até 9 anos é MIRIM; até 14 anos é INFANTIL, até 19 anos é JUNIOR, até 25 anos é SÊNIOR; acima é MASTER.
ano = int(input("Informe o ano de seu nascimento:"))
idade = 2025 - ano
if idade <= 9:
    print("Você está na categoria MIRIM")
elif idade <= 14:
    print("Você está na categoria INFANTIL")
elif idade <= 19:
    print("Você está na categoria JUNIOR")
elif idade <= 25:
    print("Você está na categoria SÊNIOR")
else:
    print("Você está na categoria MASTER")