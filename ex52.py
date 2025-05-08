# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input("Informe um número inteiro:"))
primo = True
if n <= 1:
    primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
if primo:
    print(f"{n} é um número Primo")
else:
    print(f"{n} não é um número Primo")