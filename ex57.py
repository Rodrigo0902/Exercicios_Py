# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M"ou "F".
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input("Informe seu sexo (M para masculino e F para feminino):").upper()
while sexo not in ('M', 'N'):
    print("Sexo inválido, tente novamente.")
    sexo = input("Informe seu sexo (M para masculino e F para feminino):").upper()
if sexo == 'M':
    print("Sexo selecionado: Masculino")
else:
    print("Sexo selecionado: Feminino")