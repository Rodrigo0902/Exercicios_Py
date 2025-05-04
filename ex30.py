# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input("Informe um número:"))
num = num/2
if not num.is_integer():
    print("Este número é ímpar.")
else:
    print("Este número é par.")