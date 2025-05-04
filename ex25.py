# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"no nome.
nome = input("Informe seu nome:").upper()
if 'SILVA' in nome:
    print("O nome possui o sobrenome Silva.")
else:
    print("O nome não possui o sobrenome Silva.")