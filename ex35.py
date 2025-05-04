# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input("Informe o primeiro lado:"))
b = float(input("Informe o segundo lado:"))
c = float(input("Informe o terceiro lado:"))
if a + b > c or b + c > a or a + c > b:
    print("Esse triângulo pode existir.")
else:
    print("Esse triângulo não pode existir.")