# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque: 10% DE DESCONTO;
# à vista no cartão: 5 DE DESCONTO; em até 2x no cartão: PREÇO NORMAL; 3x ou mais no cartão: 20% DE JUROS.
import os
valor = float(input("Informe o valor do produto:"))
os.system('cls')
print("Selecione qual a forma de pagamento")
print("1 - À vista Dinheiro/Cheque - 10% Desconto")
print("2 - À vista Cartão - 5% Desconto")
print("3 - 2x no Cartão - Preço normal")
print("4 - 3x ou mais no Cartão - 20% Juros")
opc = int(input())
while opc not in (1, 2, 3, 4):
    os.system('cls')
    print("Opção inválida.")
    print("Selecione qual a forma de pagamento")
    print("1 - À vista Dinheiro/Cheque - 10% Desconto")
    print("2 - À vista Cartão - 5% Desconto")
    print("3 - 2x no Cartão - Preço normal")
    print("4 - 3x ou mais no Cartão - 20% Juros")
    opc = int(input())
os.system('cls')
if opc == 1:
    valor = valor*0.9
    print(f"Valor finaL: {valor:.2f}")
elif opc == 2:
    valor = valor*0.95
    print(f"Valor finaL: {valor:.2f}")
elif opc == 3:
    print(f"Valor finaL: {valor:.2f}")
elif opc == 4:
    valor = valor*1.2
    print(f"Valor finaL: {valor:.2f}")