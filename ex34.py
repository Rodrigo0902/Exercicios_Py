# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores o iguais, o aumento é de 15%.
sal = float(input("Informe seu salário:"))
if sal <= 1250:
    sal = sal*1.15
    print(f"Seu salário com reajuste fica: {sal:.2f}")
else:
    sal = sal*1.1
    print(f"Seu salário com reajuste fica: {sal:.2f}")